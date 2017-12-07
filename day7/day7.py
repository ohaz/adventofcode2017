import re
from collections import Counter


class Node:
    def __init__(self, name, weight, children):
        self.children = children
        self.name = name
        self.weight = int(weight)
        self.children_obj = list()
        self.parent = None
        self.sum_weight = 0

    def transform_children(self, node_list):
        for child in self.children:
            for node in node_list:
                if node.name == child:
                    self.children_obj.append(node)
                    node.parent = self
                    break

    def __str__(self):
        return '{} ({}) -> {}'.format(self.name, self.weight, self.children)

    def __repr__(self):
        return str(self)


def check_weight(node):
    for child in node.children_obj:
        solution = check_weight(child)
        if solution is not None:
            return solution

    weights = [child.sum_weight for child in node.children_obj]

    node.sum_weight = sum(weights) + node.weight

    if len(weights) > 0 and max(weights) != min(weights):
        # We are going through the tree bottom up,
        # so the first "wrong" value is the correct one to balance the whole tree
        counter = Counter(weights)
        max_counter = max(counter, key=counter.get)
        min_counter = min(counter, key=counter.get)
        node_index = weights.index(min_counter)
        wrong_one = node.children_obj[node_index]
        should_be = (max_counter, min_counter, max_counter - min_counter, wrong_one.weight)
        return wrong_one, should_be
    return None


def calculate_solution():
    content = None
    with open('day7/day7_input.txt', 'r') as f:
        content = f.read()
    if content is None:
        return 'Error reading file', None

    regex = re.compile('(\w*)\s\((\d*)\)(?:\s->\s)*(.*)')
    nodes = []

    for findings in regex.findall(content):
        nodes.append(Node(findings[0], findings[1], findings[2].split(', ')))

    root = None
    for node in nodes:
        node.transform_children(nodes)

    for node in nodes:
        if node.parent is None:
            root = node
            break

    result_2 = check_weight(root)

    return root.name, '{} -> {}'.format(result_2[0].name,
                                        'Should have sum: {}, has sum: {}, So weight: {} {} = {}'.format(
                                            result_2[1][0], result_2[1][1], result_2[1][3], result_2[1][2],
                                            result_2[1][3] + result_2[1][2]
                                        ))
