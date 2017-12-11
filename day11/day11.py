import collections

# As a pen&paper player, hex grids are nothing new
# They can be handled like a 3D coordinate system with cubes in it
# When looking at the cubes from the "pointy" side and removing cubes until you have a
# plane (with pointy ends), each "cube" in that plane can be flattened to a hexagon
# This means that 3D coordinates can be used easily to get a 2D representation of a hex grid
# Examples and explanations are on https://www.redblobgames.com/grids/hexagons/
#
#             x = 0
#            \ n  /
#          nw +--+ ne
#      z = 0 /y   \ y = 0
#          -+     x+-
#      y = 0 \z   / z = 0
#          sw +--+ se
#            / s  \
#            x = 0

Point = collections.namedtuple('Point', ['x', 'y', 'z'])


def add_point(p1: Point, p2: Point):
    if p2 is None:
        print('Did not add anything')
        return p1
    return Point(x=p1.x + p2.x, y=p1.y+p2.y, z=p1.z+p2.z)


def distance(p1: Point, p2: Point):
    # The Manhattan distance in a hex grid is half the Manhattan distance in a cube grid.
    # coincidentally this is also just the max of the three distances
    return max(abs(p1.x - p2.x), abs(p1.y - p2.y), abs(p1.z - p2.z))


def calculate_solution():
    with open('day11/day11_input.txt', 'r') as f:
        content = f.read()

    steps = content.split(',')
    max_distance = 0

    zero = Point(x=0, y=0, z=0)
    current_pos = Point(x=0, y=0, z=0)

    for step in steps:
        modifier = None
        # Go around clockwise and create modify vectors
        if step == 'n':
            modifier = Point(x=0, y=1, z=-1)
        elif step == 'ne':
            modifier = Point(x=1, y=0, z=-1)
        elif step == 'se':
            modifier = Point(x=1, y=-1, z=0)
        elif step == 's':
            modifier = Point(x=0, y=-1, z=1)
        elif step == 'sw':
            modifier = Point(x=-1, y=0, z=1)
        elif step == 'nw':
            modifier = Point(x=-1, y=1, z=0)
        else:
            print('Unknown direction', step)

        current_pos = add_point(current_pos, modifier)
        max_distance = max(max_distance, distance(current_pos, zero))

    return distance(current_pos, zero), max_distance
