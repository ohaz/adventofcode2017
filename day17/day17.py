from collections import deque


def calculate_solution():
    content = 348
    spinlock = deque([0])
    for i in range(1, 2018):
        spinlock.rotate(content)
        spinlock.insert(0, i)

    solution_1 = spinlock[-1]

    spinlock = deque([0])
    for i in range(1, 50_000_001):
        spinlock.rotate(content)
        spinlock.insert(0, i)

    return solution_1, spinlock[spinlock.index(0) - 1]