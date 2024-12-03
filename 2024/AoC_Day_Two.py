import re

day = "Day Two"


# Check if row of reports is valid
def check(row) -> bool:
    results = set( [ row[i + 1] - row[i] for i in range(len(row) - 1) ] )
    
    if results <= {1, 2, 3} or results <= {-1, -2, -3}:
        return True
    else:
        return False


# Part 1 Loop
def partOne(data) -> None:
    ans = 0

    for r,row in enumerate(data):
        if check(row):
            ans += 1

    print("Part One:", ans)


# Part 2 Loop ROW 673
def partTwo(data) -> None:
    ans = 0
    
    for row in data:
        checks = list()

        for i in range(len(row)):
            clone = list(row)
            clone.pop(i)
            
            checks.append(check(clone))

        if any(checks):
            ans += 1

    print("Part Two:", ans)


if __name__ == "__main__":
    data = [ [ int(num) for num in re.split(r' ', row) ] for row in open("AOC 2024/data/" + day + ".txt").read().strip().splitlines() ]

    partOne(data)
    partTwo(data)