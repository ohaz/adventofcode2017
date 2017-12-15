def generator(start_value, factor, modulo, return_mod):
    current_value = start_value
    result_counter = 0
    while result_counter < 5000000:
        current_value = (current_value * factor) % modulo
        if current_value % return_mod == 0:
            yield current_value & 0xFFFF
            result_counter += 1


def calculate_solution():
    with open('day15/day15_input.txt', 'r') as f:
        content = f.read().splitlines()

    inputs = [int(x.split(' ')[4]) for x in content]

    same = []

    current_value_a, current_value_b = inputs[0], inputs[1]
    factor_a, factor_b = 16807, 48271

    divider = 2147483647

    for i in range(40000000):
        next_a = (current_value_a * factor_a) % divider
        next_b = (current_value_b * factor_b) % divider

        if next_a & 0xFFFF == next_b & 0xFFFF:
            same.append((next_a, next_b))

        current_value_a = next_a
        current_value_b = next_b

    same_2 = []

    current_value_a, current_value_b = inputs[0], inputs[1]

    for a, b in zip(generator(current_value_a, factor_a, divider, 4), generator(current_value_b, factor_b, divider, 8)):
        if a == b:
            same_2.append((a, b))

    return len(same), len(same_2)
