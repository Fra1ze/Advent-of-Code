import re


# Part One
def partOne(data):
    numbers_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    pairs = numbers_regex.findall(data)
    ans = 0

    for a, b in pairs:
        ans += int(a) * int(b)

    print("Part One:", ans)


# Part Two
def partTwo(data):
    numbers_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    groups = re.split(r'don\'t\(\)', data)
    ans = 0

    for i,group in enumerate(groups):
        splits = re.split(r'do\(\)', group)

        if i == 0:
            pairs = numbers_regex.findall(group)

            for a, b in pairs:
                ans += int(a) * int(b)

        elif len(splits) > 1:
            for match in splits[1:]:
                pairs = numbers_regex.findall(match)

                for a, b in pairs:
                    ans += int(a) * int(b)

    print("Part Two:", ans)


if __name__ == "__main__":
    data = open("2024/data/Day Three.txt").read()

    partOne(data)
    partTwo(data)