from day10.day10 import iterate, sparse_hash


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.group = None
        self.neighbours = []

    def flood_neighbours(self):
        for neighbour in self.neighbours:
            if neighbour.group != self.group:
                neighbour.group = self.group
                neighbour.flood_neighbours()

    def distance(self, p):
        return abs(p.x-self.x) + abs(p.y - self.y)

    def __str__(self):
        return '{}/{} - {}'.format(self.x, self.y, self.group)

    def __repr__(self):
        return str(self)


def create_points(number: int, row: int):
    points = []
    x = 0
    while number:
        if number & 1:
            points.append(Point(x, row))
        number >>= 1
        x += 1
    return points


def calculate_solution():
    content = 'oundnydw'
    hashes = [content+'-'+str(i) for i in range(128)]
    used = 0
    points = []
    for row, input_hash in enumerate(hashes):
        input_lengths_ascii = [ord(x) for x in input_hash]
        input_lengths_ascii.extend([17, 31, 73, 47, 23])

        intermediate_result_2 = iterate(input_lengths_ascii, 64)
        hashed = sparse_hash(intermediate_result_2, 16)
        number = int.from_bytes(bytearray(hashed), byteorder='big', signed=False)
        local_points = create_points(number, row)
        used += len(local_points)
        points.extend(local_points)

    group_counter = 0
    for key, point in enumerate(points):
        if point.group is None:
            point.group = group_counter
            group_counter += 1

        for other_point in points[key+1:]:
            if point.distance(other_point) == 1:
                if point not in other_point.neighbours:
                    other_point.neighbours.append(point)
                    point.neighbours.append(other_point)
                if other_point.group is None:
                    other_point.group = point.group
                else:
                    other_point.group = point.group
                    other_point.flood_neighbours()

    regions_in_use = []
    for point in points:
        if point.group not in regions_in_use:
            regions_in_use.append(point.group)

    return used, len(regions_in_use)
