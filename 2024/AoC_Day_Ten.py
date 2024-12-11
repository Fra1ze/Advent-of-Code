from collections import deque

# Part One
def partOne(data) -> list():
    ans = 0
    max_y = len(data)
    max_x = len(data[0])
    start_points = list()

    for y, row in enumerate(data):
        for x, num in enumerate(row):
            if num == 0:
                start_points.append((x, y))

    for start_point in start_points:
        endpoints = set()
        visited = set()
        queue = deque([start_point])

        while queue:
            x, y = queue.popleft()
            val = data[y][x]
            cardinals = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

            for nx, ny in cardinals:
                if 0 <= nx < max_x and 0 <= ny < max_y:
                    if (nx, ny) in visited:
                        continue

                    if val == 8 and data[ny][nx] == 9:
                        endpoints.add((nx, ny))
                    
                    elif data[ny][nx] == val + 1:
                        queue.append((nx, ny)) 

        ans += len(endpoints)

    print("Part One", ans)


# Part Two
def partTwo(data) -> None:
    ans = 0
    max_y = len(data)
    max_x = len(data[0])
    start_points = list()

    for y, row in enumerate(data):
        for x, num in enumerate(row):
            if num == 0:
                start_points.append((x, y))

    for start_point in start_points:
        endpoints = set()
        visited = { start_point: 1 }
        queue = deque([start_point])

        while queue:
            x, y = queue.popleft()
            val = data[y][x]
            cardinals = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

            if data[y][x] == 9:
                ans += visited[(x, y)]

            for nx, ny in cardinals:
                if 0 <= nx < max_x and 0 <= ny < max_y:
                    if data[ny][nx] == val + 1:
                        if (nx, ny) in visited:
                            visited[(nx, ny)] += visited[(x, y)]
                            continue

                        visited[(nx, ny)] = visited[(x, y)]
                        queue.append((nx, ny)) 

    print("Part Two", ans)


if __name__ == "__main__":
    data = [ [ int(i) for i in line.strip() ] for line in open("2024/data/Day Ten.txt").readlines() ]

    partOne(data)
    partTwo(data)