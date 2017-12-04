def calculate_solution():
    content = None
    valids_1 = 0
    with open('day4/day4_input.txt', 'r') as f:
        content = f.read()
    if content is None:
        return 'Error'

    for line in content.splitlines():
        phrases = line.split()
        if len(phrases) == len(set(phrases)):
            valids_1 += 1

    valids_2 = 0
    for line in content.splitlines():
        phrases = [sorted([y for y in x]) for x in line.split()]
        tuples = [tuple(x) for x in phrases]
        if len(phrases) == len(set(tuples)):
            valids_2 += 1

    return valids_1, valids_2
