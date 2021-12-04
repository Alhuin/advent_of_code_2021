from pprint import pprint


def ex_01(data: list[(str, int)]) -> int:
    pos_x = 0
    pos_y = 0
    for direction, step in data:
        match direction:
            case 'forward':
                pos_x += step
            case 'up':
                pos_y -= step
            case 'down':
                pos_y += step
    return pos_x * pos_y


def ex_02(data: list[(str, int)]) -> int:
    pos_x = 0
    pos_y = 0
    aim = 0
    for direction, step in data:
        match direction:
            case 'forward':
                pos_x += step
                pos_y += aim * step
            case 'up':
                aim -= step
            case 'down':
                aim += step
    return pos_x * pos_y


def main(data_path, expected_1, expected_2):
    with open(data_path, encoding="utf-8") as file:
        dataset = [
            line.split(' ')
            for line in file.read().split('\n')[:-1]
        ]
        dataset = [[data[0], int(data[1])] for data in dataset]

    assert ex_01(dataset) == expected_1
    assert ex_02(dataset) == expected_2


if __name__ == '__main__':
    main('resources/example.txt', expected_1=150, expected_2=900)
    main('resources/input.txt', expected_1=1507611, expected_2=1880593125)
