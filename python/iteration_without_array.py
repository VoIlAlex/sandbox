

if __name__ == "__main__":
    a0 = 0
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 4
    for i in range(5):
        var_name = 'a' + str(i)
        var_value = locals()[var_name]
        print(var_value)
