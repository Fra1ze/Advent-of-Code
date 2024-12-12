from functools import cache

# Process stone and return number of stones from chain
@cache
def processStone(stone, i) -> list:
    if i == 0:
        return 1

    if stone == "0":
        return processStone("1", i - 1)

    elif len(stone) % 2 == 0:
        half = len(stone) // 2
        stone_a, stone_b = str(int(stone[:half])), str(int(stone[half:]))
    
        return sum([processStone(stone_a, i - 1), processStone(stone_b, i - 1)])

    else:
        return processStone(str(int(stone) * 2024), i - 1)

# Part One
def partOne(data) -> None:
    stones = data

    for i in range(25):
        new_stones = list()
        
        for stone in stones:
            if stone == "0":
                new_stones.append("1")

            elif len(stone) % 2 == 0:
                half = len(stone) // 2
                stone_a, stone_b = str(int(stone[:half])), str(int(stone[half:]))

                new_stones += [stone_a, stone_b]

            else:
                new_stones.append(str(int(stone) * 2024))

        stones = new_stones

    print("Part One:", len(stones))

        
# Part Two
def partTwo(data) -> None:
    ans = 0

    for stone in data:
        ans += processStone(stone, 75)

    print("Part Two:", ans)


if __name__ == "__main__":
    data = [ num for line in open("2024/data/Day Eleven.txt") for num in line.split() ]

    partOne(data)
    partTwo(data)