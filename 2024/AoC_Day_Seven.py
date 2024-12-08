import math

# Creates Ternary string
def toTernary (num):
    nums = []

    if num == 0:
        return '0'
    
    while num:
        num, r = divmod(num, 3)
        nums.append(str(r))
        
    return ''.join(reversed(nums))


# Check if any permutation is valid
def calculate(total, nums, permutations) -> bool:
    for permutation in permutations:
        n = nums.copy()
        t = n.pop(0)

        for i, num in enumerate(n):
            if permutation[i] == "0":
                t += num

            elif permutation[i] == "1":
                t *= num

            elif permutation[i] == "2":
                t = int(str(t) + str(num))

        if t == total:
            return True
    
    return False


# Part One
def partOne(data) -> None:
    ans = 0
    
    for total, nums in data:
        base_val = len( nums ) - 1
        permutations = [ str( bin(i) )[2:].zfill(base_val) for i in range( ( 2 ** base_val ) )]

        if calculate(total, nums, permutations):
            ans += total

    print("Part One:", ans)


# Part Two
def partTwo(data) -> list:
    ans = 0

    for total, nums in data:
        base_val = len( nums ) - 1
        permutations = [ str( toTernary(i) ).zfill(base_val) for i in range( ( 3 ** base_val ) )]

        if calculate(total, nums, permutations):
            ans += total

    print("Part Two:", ans)


if __name__ == "__main__":
    data = [ ( int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())) ) for line in open("2024/data/Day Seven.txt").readlines() ]

    partOne(data)
    partTwo(data)