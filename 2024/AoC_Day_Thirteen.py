import re

def partOne(machines):
    prizes_count = 0
    tokens_used = 0
    # 10000000000000
    for x1, y1, x2, y2, px, py in machines:
        ac = (px * y2 - py * x2) / (x1 * y2 - y1 * x2)
        bc = (px - x1 * ac) / x2
        
        if ac % 1 == 0 and ac < 101 and bc % 1 == 0 and bc < 101:
            prizes_count += 1
            tokens_used += (int(ac) * 3) + int(bc)

    print(f'Part One: {tokens_used} tokens for {prizes_count} prizes')


def partTwo(machines):
    prizes_count = 0
    tokens_used = 0
    
    for x1, y1, x2, y2, px, py in machines:
        px = px + 10_000_000_000_000
        py = py + 10_000_000_000_000

        ac = (px * y2 - py * x2) / (x1 * y2 - y1 * x2)
        bc = (px - x1 * ac) / x2
        
        if ac % 1 == 0 and bc % 1 == 0:
            prizes_count += 1
            tokens_used += (int(ac) * 3) + int(bc)

    print(f'Part Two: {tokens_used} tokens for {prizes_count} prizes')


if __name__ == "__main__":
    numbers_regex = re.compile(r'\d+')
    machines = [ list(map(int, numbers_regex.findall(block))) for block in open("./2024/data/Day Thirteen.txt").read().split("\n\n") ]
    
    partOne(machines)
    partTwo(machines)