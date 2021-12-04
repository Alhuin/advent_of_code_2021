from day_04.models import Grid
from day_04.utils import parse


def play(drawns: list[int], grids: list[Grid], win_condition: callable) -> int:
    for drawn in drawns:
        for grid in grids:
            grid.mark(drawn)
            if not win_condition(grid, grids):
                continue
            return grid.compute_score(drawn)


def ex_01(drawns: list[int], grids: list[Grid]) -> int:
    return play(
        drawns,
        grids,
        lambda x, _: x.self_check()
    )


def ex_02(drawns: list[int], grids: list[Grid]) -> int:
    return play(
        drawns,
        grids,
        lambda x, y: x.self_check() and all(grid.won for grid in y)
    )


def main(data_path, expected_1, expected_2):
    with open(data_path, encoding="utf-8") as file:
        dataset = [
            line.split(' ')
            for line in file.read().split('\n')[:-1] if line != ''
        ]
    drawns, grids = parse(dataset)

    assert ex_01(drawns, grids) == expected_1
    assert ex_02(drawns, grids) == expected_2


if __name__ == "__main__":
    main('resources/example.txt', expected_1=4512, expected_2=1924)
    main('resources/input.txt', expected_1=29440, expected_2=13884)
