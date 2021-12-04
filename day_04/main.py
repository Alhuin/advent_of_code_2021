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


if __name__ == "__main__":
    with open('input.txt', encoding="utf-8") as file:
        dataset = [
            line.split(' ')
            for line in file.read().split('\n')[:-1] if line != ''
        ]
    drawns, grids = parse(dataset)

    print(ex_01(drawns, grids))
    # print(ex_02(drawns, grids))
