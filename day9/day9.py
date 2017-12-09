
def handle_group(content, index, depth):
    result = depth
    garbage_mode = False
    ignore_mode = False
    child_consumed = 0
    consumed = 0
    garbage_consumed = 0
    for i in range(index, len(content)):
        char = content[i]
        consumed += 1
        if child_consumed > 0:
            child_consumed -= 1
            continue
        if ignore_mode:
            ignore_mode = False
            continue
        if char == '!':
            ignore_mode = True
            continue
        if garbage_mode:
            if char != '>':
                garbage_consumed += 1
                continue
            garbage_mode = False
            continue
        if char == '<':
            garbage_mode = True
            continue

        if char == '{':
            result_child = handle_group(content, i + 1, depth+1)
            child_consumed += result_child[1]
            result += result_child[0]
            garbage_consumed += result_child[2]
        if char == '}':
            return result, consumed, garbage_consumed
        if char == ',':
            continue
    return result, consumed, garbage_consumed


def calculate_solution():

    with open('day9/day9_input.txt', 'r') as f:
        content = f.read()

    result = handle_group(content, 0, 0)
    return result[0], result[2]
