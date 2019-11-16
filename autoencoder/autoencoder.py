import torch
import numpy as np

import distrdata
import matplotlib.pyplot as plt


class OneHiddenLayerEncoding(torch.nn.Module):
    def __init__(self, hidden_size):
        torch.nn.Module.__init__(self)
        self.l1 = torch.nn.Linear(100, hidden_size)
        self.l2 = torch.nn.Linear(hidden_size, 100)

    def forward(self, X):
        X = self.l1(X)
        X = self.l2(X)
        return X


if __name__ == "__main__":
    dataset = distrdata.generate_dataset_normal((-5, 5, 0.1),
                                                noise_radius=0.0)
    input = dataset[:, 1]
    input = np.expand_dims(input, axis=0)
    input = torch.from_numpy(input).float()

    # array of losses
    # with different sizes
    # of the hidden layer
    min_losses = []

    for hidden_size in np.arange(10, 500, 10):
        net = OneHiddenLayerEncoding(
            hidden_size=hidden_size
        )
        optimizer = torch.optim.SGD(params=net.parameters(), lr=0.02)
        criterion = torch.nn.MSELoss()
        min_loss = None
        for i in range(1000):
            output = net(input)
            loss = criterion(output, input)
            loss.backward()
            optimizer.step()
            min_loss = loss if min_loss is None else min(loss, min_loss)
        min_losses.append(min_loss)
        print('Hidden size: {}\n Min loss: {}'.format(hidden_size, min_loss))
    plt.plot(min_losses)
    plt.show()
