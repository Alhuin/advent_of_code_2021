def ex_01(data: list[str]) -> int:
    cols = zip(*data)
    gamma_bit = ''
    epsilon_bit = ''
    for col in cols:
        gamma_bit += max(col, key=col.count)
        epsilon_bit += '0' if gamma_bit[-1] == '1' else '1'
    return int(gamma_bit, 2) * int(epsilon_bit, 2)


def get_rating(solutions: list[str], condition: callable, i: int) -> int:
    return int(solutions[0], 2) if len(solutions) == 1 else get_rating(
        [sol for sol in solutions if sol[i] == condition(list(zip(*solutions))[i])],
        condition,
        i + 1
    )


def ex_02(data: list[str]) -> int:
    co2_rating = get_rating(
        data,
        lambda x: min(x, key=x.count) if max(x, key=x.count) != min(x, key=x.count) else '0',
        0
    )
    oxygen_rating = get_rating(
        data,
        lambda x: max(x, key=x.count) if max(x, key=x.count) != min(x, key=x.count) else '1',
        0
    )
    return co2_rating * oxygen_rating


def main(data_path, expected_1, expected_2):
    with open(data_path, encoding="utf-8") as file:
        dataset = file.read().split('\n')[:-1]

    assert ex_01(dataset) == expected_1
    assert ex_02(dataset) == expected_2


if __name__ == "__main__":
    main('resources/example.txt', expected_1=198, expected_2=230)
    main('resources/input.txt', expected_1=2498354, expected_2=3277956)
