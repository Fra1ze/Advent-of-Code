# Part One
def partOne(data) -> None:
    antennas = dict()
    antinodes = set()

    for y, row in enumerate(data):
        for x, ch in enumerate(row):
            if ch != ".":
                if ch not in antennas:
                    antennas[ch] = list()

                antennas[ch].append((x, y))

    for antenna_list in antennas.values():
        for i in range(len(antenna_list)):
            x1, y1 = antenna_list[i]

            for j in range(i + 1, len(antenna_list)):
                x2, y2 = antenna_list[j]
                possible_nodes = [ (2 * x1 - x2, 2 * y1 - y2), (2 * x2 - x1, 2 * y2 - y1) ]
                
                for x3, y3 in possible_nodes:
                    if 0 <= x3 < len(data[0]) and 0 <= y3 < len(data):
                        antinodes.add((x3, y3))

    print("Part One:", len(antinodes))
                

# Part Two
def partTwo(data) -> None:
    antennas = dict()
    antinodes = set()

    for y, row in enumerate(data):
        for x, ch in enumerate(row):
            if ch != ".":
                if ch not in antennas:
                    antennas[ch] = list()

                antennas[ch].append((x, y))

    for antenna_list in antennas.values():
        for i in range(len(antenna_list)):
            x1, y1 = antenna_list[i]

            for j in range(len(antenna_list)):
                x2, y2 = antenna_list[j]

                if i != j:
                    x, y = x1, y1
                    xt = x2 - x1
                    yt = y2 - y1

                    while 0 <= x < len(data[0]) and 0 <= y < len(data):
                        antinodes.add((x,y))
                        x += xt
                        y += yt


    print("Part Two:", len(antinodes))


if __name__ == "__main__":
    data = [ [ch for ch in line.strip() ] for line in open("2024/data/Day Eight.txt").readlines() ]

    partOne(data)
    partTwo(data)