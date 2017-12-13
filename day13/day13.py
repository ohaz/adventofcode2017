def calculate_solution():
    with open('day13/day13_input.txt', 'r') as f:
        content = f.read().splitlines()

    d = {}

    for line in content:
        left, right = line.split(': ')
        d[int(left)] = int(right)

    severity = 0

    for key in d.keys():
        if key % (2*d[key] - 2) == 0:
            severity += key*d[key]

    delay = 0
    finished = False
    while not finished:

        finished = True

        for key in d.keys():
            entry = d[key]
            pos = (key + delay) % (2 * entry - 2)
            if pos == 0:
                finished = False
                delay += 1
                break

    return severity, delay
