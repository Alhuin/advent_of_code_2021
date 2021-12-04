from day_04.models import Grid, GridPoint


def parse(data: list[list[str]]) -> (list[int], list[Grid]):
    drawns_line = data[0][0]
    grid_lines = data[1:]
    drawns = [int(value) for value in drawns_line.split(',')]
    grids = [
        Grid([
            [GridPoint(int(value)) for value in line if value != '']
            for line in grid_lines[x:x+5]
        ])
        for x in range(len(grid_lines)) if not x % 5
    ]
    return drawns, grids
