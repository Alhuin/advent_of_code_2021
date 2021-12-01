def ex_01(data):
    return sum(1 for i in range(len(data) - 1) if data[i] < data[i + 1])


def ex_02(data, n):
    return ex_01([sum(data[i:n + i]) for i in range(len(data) - n + 1)])


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.read().split('\n')

    data = [int(value) for value in data[:-1]]

    ex_01(data)
    print(ex_02(data, 3))
