def calculate_solution():
    searching_for = 312051

    # part 1

    ring_sum = 1
    ring = 1
    ring_starts = 0
    width = 1
    while ring_sum < searching_for:
        width += 2
        ring += 1
        new_ring_sum = width**2
        ring_starts = ring_sum + 1
        ring_sum = new_ring_sum

    middle = ring_starts + int(width / 2) - 1
    prev_middle = middle
    while searching_for > middle:
        prev_middle = middle
        middle += width - 1
    distance_1 = ring - 1 + min(abs(middle - searching_for), abs(prev_middle - searching_for))

    # Part 2

    grid = [[0 for _ in range(700)] for _ in range(700)]
    x, y = 350, 350
    center = 350
    grid[x][y] = 1
    value_written = 1
    width = 1
    ring = 0
    while value_written < searching_for:
        width += 2
        ring += 1
        while x < center + ring:
            x += 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break
        while y < center + ring:
            y += 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break
        while x > center - ring:
            x -= 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break
        while y > center - ring:
            y -= 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break
        while x < center + ring:
            x += 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break

    return distance_1, value_written


def sum_around(grid, x, y):
    try:
        return grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y-1] + grid[x-1][y] + grid[x-1][y-1] + grid[x-1][y+1] + grid[x][y-1] + grid[x][y+1]
    except:
        print(x, y)
        exit()
