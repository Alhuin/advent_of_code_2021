def ex_01(dataset: list[int]) -> int:
    return get_nb_fishes(dataset, 80)


def ex_02(dataset: list[int]) -> int:
    return get_nb_fishes(dataset, 256)


def get_nb_fishes(data: list[int], days: int = 18) -> int:
    nb_fish_by_state = [0 for _ in range(9)]
    for fish_state in data:
        nb_fish_by_state[fish_state] += 1
    for day in range(days):
        fishes_at_0 = nb_fish_by_state.pop(0)           # get fishes at state 0 and remove the col
        nb_fish_by_state += [fishes_at_0]               # new_children == nb_previous_0, so add new_children at index 8
        nb_fish_by_state[6] += fishes_at_0              # add nb_previous_0 at index 6
    return sum(nb_fish_by_state)


def main(data_path, expected_1, expected_2):
    with open(data_path, encoding='utf-8') as file:
        dataset = [
            int(timer)
            for timer in file.read().split('\n')[0].split(',')
        ]

    assert ex_01(dataset) == expected_1
    assert ex_02(dataset) == expected_2


if __name__ == '__main__':
    main('resources/example.txt', expected_1=5934, expected_2=26984457539)
    main('resources/input.txt', expected_1=365862, expected_2=1653250886439)
