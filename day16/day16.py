from collections import deque
import string


def dance(n: int, circular_list, content):
    seen = []
    for current in range(n):
        result = ''.join(circular_list)
        if result in seen:
            return seen[n % current]

        seen.append(result)

        for step in content:
            if step[0] == 's':
                circular_list = deque(circular_list)
                circular_list.rotate(int(step[1:]))
                circular_list = list(circular_list)
            elif step[0] == 'x':
                numbers = [int(x) for x in step[1:].split('/')]
                circular_list[numbers[0]], circular_list[numbers[1]] = circular_list[numbers[1]], circular_list[
                    numbers[0]]
            elif step[0] == 'p':
                spots = [circular_list.index(x) for x in step[1:].split('/')]
                circular_list[spots[0]], circular_list[spots[1]] = circular_list[spots[1]], circular_list[spots[0]]
            else:
                print('Unknown command', step)
    return circular_list


def calculate_solution():
    with open('day16/day16_input.txt', 'r') as f:
        content = f.read().strip().split(',')

    alph = list(string.ascii_lowercase)[:16]

    result1 = dance(1, alph[:], content)
    result2 = dance(1000000000, alph[:], content)

    return ''.join(result1), result2
