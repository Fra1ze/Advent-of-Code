import re

day = "Day One"


# Part One
def partOne(data) -> None:
    left, right = data

    print("Part One:", sum([ abs(left[i] - right[i]) for i in range(len(left)) ]))


# Part Two
def partTwo(data) -> None:
    left, right = data
    ans = 0

    print(sum([num * right.count(num) for num in left]))


if __name__ == "__main__":
    data = list( map(sorted, list( zip(*[ map( int, line.split() ) for line in open("AOC 2024/data/" + day + ".txt").read().strip().splitlines() ]) )) )
    
    partOne(data)
    partTwo(data)