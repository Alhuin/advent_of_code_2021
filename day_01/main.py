def ex_01(data: list[int]) -> int:
    return sum(1 for i in range(len(data) - 1) if data[i] < data[i + 1])


def ex_02(data: list[int], window: int) -> int:
    return ex_01([sum(data[i:window + i]) for i in range(len(data) - window + 1)])


def main(data_path, expected_1, expected_2):
    with open(data_path, encoding="utf-8") as file:
        dataset = [int(value) for value in file.read().split('\n')[:-1]]

    assert ex_01(dataset) == expected_1
    assert ex_02(dataset, 3) == expected_2


if __name__ == '__main__':
    main('resources/example.txt', expected_1=7, expected_2=5)
    main('resources/input.txt', expected_1=1553, expected_2=1597)
