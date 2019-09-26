"""

    Here I try to plot 
    probability grid of 
    beeing in the class of
    walkers or drivers.

"""


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2


class ClassificationProbabilityGrid:
    def __init__(self, X, y, radius=40, grid_size=(400, 400)):
        self.grid_size = grid_size

        self.X = X

        # scaling to fit
        # into the grid
        self.X += np.min(self.X)
        self.X *= grid_size[0] / np.max(self.X)
        self.X = self.X.astype('uint8')

        self.y = y
        self.radius = radius

    def __walkers(self):
        walkers_count = 0
        for point_class in self.y:
            if point_class == 0:
                walkers_count += 1
        return walkers_count

    def __drivers(self):
        drivers_count = 0
        for point_class in self.y:
            if point_class == 1:
                drivers_count += 1
        return drivers_count

    def __walkers_inside_circle_probability(self, center):
        walkers_count = 0
        walkers_inside_circle_count = 0
        for x, point_class in zip(self.X, self.y):
            if np.linalg.norm(x - center) < self.radius:
                walkers_inside_circle_count += 1
            walkers_count += 1
        return walkers_inside_circle_count / walkers_count

    def __drivers_inside_circle_probability(self, center):
        drivers_count = 0
        drivers_inside_circle_count = 0
        for x, point_class in zip(self.X, self.y):
            if np.linalg.norm(x - center) < self.radius:
                drivers_inside_circle_count += 1
            drivers_count += 1
        return drivers_inside_circle_count / drivers_count

    def __walkers_probability(self):
        return self.__walkers() / len(self.y)

    def __drivers_probability(self):
        return self.__drivers() / len(self.y)

    def __circle_probability(self, center):
        walkers_inside = self.__walkers_inside_circle_probability(
            center) * self.__walkers()
        drivers_inside = self.__drivers_inside_circle_probability(
            center) * self.__drivers()
        return (walkers_inside + drivers_inside) / len(self.y)

    def numpy_walkers(self):
        grid_size = 400
        grid = np.zeros(shape=(grid_size, grid_size), dtype='uint8')
        cell_size = grid_size // 100
        point_radius = cell_size // 2
        for i in range(grid_size // cell_size):
            for j in range(grid_size // cell_size):
                # preparation of
                # the data point
                data_point = (i * cell_size, j * cell_size)

                # find the probability
                # that given data point
                # is a walker
                try:
                    prob = self.__walkers_inside_circle_probability(
                        data_point
                    ) * self.__walkers_probability() / self.__circle_probability(data_point)
                except ZeroDivisionError:
                    prob = 0

                # convertion into
                # pixel intensity
                prob = int(prob * 255)

                # draw the probability
                # on the grid
                cv2.circle(
                    img=grid,
                    center=tuple(data_point),
                    radius=int(point_radius),
                    color=prob,
                    thickness=-1
                )
        return grid

    def numpy_drivers(self):
        grid_size = 400
        grid = np.zeros(shape=(grid_size, grid_size), dtype='uint8')
        cell_size = grid_size // 100
        point_radius = cell_size // 2
        for i in range(grid_size // cell_size):
            for j in range(grid_size // cell_size):
                # preparation of
                # the data point
                data_point = (i * cell_size, j * cell_size)

                # find the probability
                # that given data point
                # is a walker
                try:
                    prob = self.__drivers_inside_circle_probability(
                        data_point
                    ) * self.__drivers_probability() / self.__circle_probability(data_point)
                except ZeroDivisionError:
                    prob = 0

                # convertion into
                # pixel intensity
                prob = int(prob * 255)

                # draw the probability
                # on the grid
                cv2.circle(
                    img=grid,
                    center=tuple(data_point),
                    radius=int(point_radius),
                    color=prob,
                    thickness=-1
                )
        return grid


if __name__ == "__main__":
    # Importing the dataset
    dataset = pd.read_csv('data/Social_Network_Ads.csv')
    X = dataset.iloc[:, [2, 3]].values
    y = dataset.iloc[:, 4].values

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0)

    # Feature Scaling
    # Feature Scaling
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    grid = ClassificationProbabilityGrid(X_train, y_train)
    drivers_probs = grid.numpy_drivers()
    cv2.namedWindow('Probabilities')
    while True:
        cv2.imshow('Probabilities', drivers_probs)
        if cv2.waitKey(100) == ord('q'):
            break
