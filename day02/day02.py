import numpy as np


def read_input():
    f = open('day02/input.txt')
    lines = f.readlines()

    cmds = []
    nums = []

    for line in lines:
        words = line.split(' ')
        cmds.append(words[0])
        nums.append(words[1])

    return cmds, nums


def parse_input(commands, numbers):
    vert = 0
    hor = 0
    for cmd, num in zip(commands, numbers):
        if cmd == 'forward':
            hor += int(num)
        elif cmd == 'down':
            vert += int(num)
        else:
            vert -= int(num)

    return hor, vert


def parse_manual(commands, numbers):
    aim = 0
    hor = 0
    depth = 0

    for cmd, num in zip(commands, numbers):
        if cmd == 'forward':
            hor += int(num)
            depth += aim * int(num)
        elif cmd == 'down':
            aim += int(num)
        else:
            aim -= int(num)
    return hor, depth


def main():
    commands, numbers = read_input()
    horizontal, vertikal = parse_input(commands, numbers)

    print(f'x: {horizontal} y: {vertikal} product: {horizontal * vertikal}')

    horizontal, vertikal = parse_manual(commands, numbers)

    print(f'x: {horizontal} y: {vertikal} product: {horizontal * vertikal}')


if __name__ == '__main__':
    main()
