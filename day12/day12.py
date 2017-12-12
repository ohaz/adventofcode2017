class Node:
    def __init__(self, id_, connected_to):
        self.id_ = id_
        self.connections = connected_to
        self.nodes = []


seen = []


def traverse_node(node: Node):
    if node.id_ in seen:
        return
    seen.append(node.id_)
    for child_node in node.nodes:
        traverse_node(child_node)


def calculate_solution():
    with open('day12/day12_input.txt', 'r') as f:
        content = f.read().splitlines()

    connections = []

    for line in content:
        left_side, right_side = line.split(' <-> ')
        connections.append(Node(int(left_side), [int(x) for x in right_side.split(', ')]))

    for connection in connections:
        for connected_node in connection.connections:
            connection.nodes.append(connections[connected_node])

    all_lists = []
    for node in connections:
        global seen
        seen = []
        traverse_node(node)
        seen = sorted(seen)
        if seen not in all_lists:
            all_lists.append(seen)

    return len(all_lists[0]), len(all_lists)
