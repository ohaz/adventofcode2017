import re
import operator
import collections


def calculate_solution():
    regex_pattern = re.compile('(\w*)\s(inc|dec)\s([-]*[0-9]*)\sif\s(\w*)\s([!><=]+)\s([-]*[0-9]*)')
    registers = collections.defaultdict(int)
    reg_max = 0

    with open('day8/day8_input.txt', 'r') as f:
        content = f.read()
    if content is None:
        return 'Could not read file', None

    instructions = {'inc': operator.add, 'dec': operator.sub}

    comparison = {'>': operator.gt, '<': operator.lt, '>=': operator.ge, '<=': operator.le, '==': operator.eq,
                  '!=': operator.ne}

    for match in regex_pattern.findall(content):

        if comparison[match[4]](registers[match[3]], int(match[5])):
            registers[match[0]] = instructions[match[1]](registers[match[0]], int(match[2]))

        reg_max = max(reg_max, registers[match[0]])

    return max(registers.values()), reg_max
