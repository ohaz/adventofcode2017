from collections import deque
import binascii


def iterate(input_lengths, amount):
    circular_list = deque(range(0, 256))
    skip_size = 0
    rotated_by = 0
    for _ in range(amount):
        for length in input_lengths:
            deque_list = list(circular_list)

            selected_area = reversed(deque_list[0:length])
            deque_list[0:length] = selected_area
            circular_list = deque(deque_list)
            rotated_by += length+skip_size
            circular_list.rotate(-(length+skip_size))

            skip_size += 1

    circular_list.rotate(rotated_by)

    deque_list = list(circular_list)

    return deque_list


def sparse_hash(intermediate_result, block_size):
    slice_hashes = []
    for i in range(block_size):
        slice_hash = 0
        for y in range(block_size):
            slice_hash ^= intermediate_result[16*i+y]
        slice_hashes.append(slice_hash)
    return slice_hashes


def calculate_solution():
    with open('day10/day10_input.txt', 'r') as f:
        content = f.read()
    try:
        input_lengths = [int(x) for x in content.split(',')]
        result_1 = iterate(input_lengths, 1)
    except ValueError:
        result_1 = [0, 0]

    input_lengths_ascii = [ord(x) for x in content]
    input_lengths_ascii.extend([17, 31, 73, 47, 23])

    intermediate_result_2 = iterate(input_lengths_ascii, 64)
    hashed = sparse_hash(intermediate_result_2, 16)

    return result_1[0]*result_1[1], binascii.hexlify(bytearray(hashed))
