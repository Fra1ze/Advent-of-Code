from collections import deque

def getRegions(garden):
    max_y = len(garden)
    max_x = len(garden[0])
    seen = []
    regions = []
    
    for r in range(max_y):
        for c in range(max_x):
            if (c, r) in seen: continue

            plant = garden[r][c]
            region = set({(c, r)})
            queue = deque([(c, r)])
            
            while queue:
                x, y = queue.popleft()

                for x_offset, y_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ox, oy = (x + x_offset, y + y_offset)

                    if 0 <= ox < max_x and 0 <= oy < max_y:
                        if garden[oy][ox] == plant and (ox, oy) not in seen:
                            seen.append((ox, oy))
                            queue.append((ox, oy))
                            region.add((ox, oy))

            regions.append(region)

    return regions


def getFenceSegments(regions):
    north, east, south, west = set(), set(), set(), set()
    
    for x, y in regions:
        if (x, y - 1) not in regions: north.add((x, y))
        if (x + 1, y) not in regions: east.add((x, y))
        if (x, y + 1) not in regions: south.add((x, y))
        if (x - 1, y) not in regions: west.add((x, y))

    return north, east, south, west


def getCorners(regions):
    north, east, south, west = getFenceSegments(regions)
    corners = []

    for x, y in north:
        if (x, y) in west:
            corners.append((x - 0.5, y - 0.5))
        if (x, y) in east:
            corners.append((x + 0.5, y - 0.5))
        if (x - 1, y - 1) in east and (x, y) not in west:
            corners.append((x - 0.5, y - 0.5))
        if (x + 1, y - 1) in west and (x, y) not in east:
            corners.append((x - 0.5, y + 0.5))

    for x, y in south:
        if (x, y) in west:
            corners.append((x - 0.5, y + 0.5))
        if (x, y) in east:
            corners.append((x + 0.5, y + 0.5))
        if (x - 1, y + 1) in east and (x, y) not in west:
            corners.append((x - 0.5, y + 0.5))
        if (x + 1, y + 1) in west and (x, y) not in east:
            corners.append((x + 0.5, y + 0.5))

    return corners


def partOne(garden):
    regions = getRegions(garden)
    total = sum([ sum([ len(fences) * len(region) for fences in getFenceSegments(region) ]) for region in regions ])

    print(f'Part One: {total}')


def partTwo(garden):
    regions = getRegions(garden)
    total = sum([ len(getCorners(region)) * len(region) for region in regions ])

    print(f'Part Two: {total}')


if __name__ == "__main__":
    data = [ [ *line ] for line in open("./2024/data/Day Twelve.txt", "r").read().splitlines() ]
    partOne(data)
    partTwo(data)
