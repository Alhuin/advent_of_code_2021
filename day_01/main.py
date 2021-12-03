def ex_01(data: list[int]) -> int:
    return sum(1 for i in range(len(data) - 1) if data[i] < data[i + 1])


def ex_02(data: list[int], window: int) -> int:
    return ex_01([sum(data[i:window + i]) for i in range(len(data) - window + 1)])


if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        dataset = [int(value) for value in file.read().split('\n')[:-1]]

    print(ex_01(dataset))
    print(ex_02(dataset, 3))
