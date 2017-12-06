from copy import copy

input_day6_1 = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]


def calculate_solution():
    start_bank = copy(input_day6_1)
    old_banks = list()

    while start_bank not in old_banks:
        old_banks.append(copy(start_bank))
        index = start_bank.index(max(start_bank))
        value, start_bank[index] = start_bank[index], 0
        while value > 0:
            index += 1
            start_bank[index % len(start_bank)] += 1
            value -= 1

    return len(old_banks), len(old_banks) - old_banks.index(start_bank)
