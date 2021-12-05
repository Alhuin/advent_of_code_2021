from day_05.models import Point


def ex_01(data: list[list[Point]], diag: bool = False) -> int:
    points_list = []
    for points in data:
        points_list = upsert_points(
            arange_points(points[0], points[1], diag),
            points_list
        )
    return sum(1 for point in points_list if point.occur > 1)


def ex_02(data: list[list[Point]]) -> int:
    return ex_01(data, diag=True)


def upsert_points(new_points: list[Point], points_list: list[Point]) -> list[Point]:
    for point in new_points:
        try:
            i = points_list.index(point)
            points_list[i].occur += 1
        except ValueError:
            points_list.append(point)
    return points_list


def arange_points(start: Point, stop: Point, diag: bool = False) -> list[Point]:
    if start.x == stop.x:
        step = Point([0, 1])
        begin = start if start.y < stop.y else stop
    elif start.y == stop.y:
        step = Point([1, 0])
        begin = start if start.x < stop.x else stop
    elif diag:
        begin = start if start.y < stop.y else stop
        end = start if begin != start else stop
        step = Point([1, 1]) if begin.x < end.x else Point([-1, 1])
    else:
        return []
    return [
        begin + step * i
        for i in range(len(stop - start) + 1)
    ]


def main(data_path, expected_1, expected_2):
    with open(data_path, encoding="utf-8") as file:
        dataset = [
            [
                Point(list(map(int, points.split(','))))
                for points in line.split(' -> ')
            ]
            for line in file.read().split('\n')[:-1]
        ]

    assert ex_01(dataset) == expected_1
    assert ex_02(dataset) == expected_2


if __name__ == "__main__":
    main('resources/example.txt', expected_1=5, expected_2=12)
    # main('resources/input.txt', expected_1=7438, expected_2=21406)  # Have a break, have a kitkat
