def ex_01(dataset: list[int], days: int = 18) -> int:
    return sum(
        1 + get_reproduction_by_fish(timer, days)
        for timer in dataset
    )


def ex_02(dataset: list[int]) -> int:
    return ex_01(dataset, 256)


def get_reproduction_by_fish(timer, days_remaining: int) -> int:
    days_remaining = days_remaining - (timer + 1)

    if days_remaining < 0:
        return 0

    produced_after_first = (days_remaining // 7)

    return 1 + produced_after_first + sum(
        get_reproduction_by_fish(8, days_remaining - 7 * i)  # timer expiration, -7, -14, -21... days_remaining < 7
        for i in range(produced_after_first)
    )


def main(data_path, expected_1):
    with open(data_path, encoding='utf-8') as file:
        dataset = [
                int(timer)
                for timer in file.read().split('\n')[0].split(',')
            ]
    # print(ex_01(dataset, 18))
    print(ex_02(dataset))
    # print(get_reproduction_by_fish(1, 2, 256))


if __name__ == '__main__':
    # main('resources/example.txt', expected_1=5934)
    main('resources/input.txt', expected_1=365862)
