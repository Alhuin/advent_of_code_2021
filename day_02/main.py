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


if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        dataset = [
            value.split(' ')
            for value in file.read().split('\n')[:-1]
        ]

    # print(ex_01([(direction, int(step)) for direction, step in dataset]))
    print(ex_02([(direction, int(step)) for direction, step in dataset]))
