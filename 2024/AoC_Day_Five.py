page_rules = None

# Part One
def partOne(data) -> None:
    to_part_two = list()
    ans = 0

    for line in data:
        valid = True
        line_rules = [ rule for rule in page_rules if rule[0] in line and rule[1] in line ]

        for num in line:
            num_rules = [ rule for rule in line_rules if rule[0] == num ]
            num_idx = line.index(num)
            
            for a, b in num_rules:
                b_idx = line.index(b)

                if b in line[:num_idx]:
                    valid = False

        if valid:
            middle_idx = (len(line) // 2 + (len(line) % 2 > 0)) - 1
            ans += line[middle_idx]
        else:
            to_part_two.append([line_rules, line])

    print("Part One:", ans)
    
    partTwo(to_part_two)


# Part Two
def partTwo(data) -> None:
    ans = 0
    
    for rules, line in data:
        while not check(rules, line):
            for a, b in rules:
                a_idx = line.index(a)
                b_idx = line.index(b)

                if a in line[b_idx:]:
                    x = line.pop(b_idx)

                    line.insert(a_idx + 1, x)

                if b in line[:a_idx]:
                    x = line.pop(a_idx)

                    line.insert(b_idx, x)

        middle_idx = (len(line) // 2 + (len(line) % 2 > 0)) - 1
        ans += line[middle_idx]
    
    print("Part Two:", ans)


# Check if line is valid
def check(rules, line) -> bool:
    valid = True
    
    for num in line:
        num_rules = [ rule for rule in rules if rule[0] == num ]
        num_idx = line.index(num)
        
        for a, b in num_rules:
            b_idx = line.index(b)

            if b in line[:num_idx]:
                valid = False

    return valid


if __name__ == "__main__":
    top, bottom = open("data/Day Five.txt").read().strip().split("\n\n")

    page_rules = [tuple(map(int, row.split("|"))) for row in top.splitlines()]
    data = [list(map(int, row.split(","))) for row in bottom.splitlines()]
    
    partOne(data)
