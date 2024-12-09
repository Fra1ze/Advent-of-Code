# Build hard drive list
def buildHardDrive(data) -> list:
    hard_drive = list()
    free_space = False
    file_id = 0

    for value in data:
        if free_space:
            for _ in range(value):
                hard_drive.append(".")
            
            free_space = False

        else:
            for _ in range(value):
                hard_drive.append(file_id)

            file_id += 1
            free_space = True

    return hard_drive


# Find first index that has enough space to fit file
def findIndex(size, drive) -> int:
    first_free = drive.index(".")

    for i in range(first_free, len(drive) - size ):
        if all( [ True if ch == "." else False for ch in drive[i:i + size] ] ): return i

    else: return False


# Part One
def partOne(data) -> None:
    hard_drive = buildHardDrive(data)

    i = len(hard_drive) - 1
    free_idx = hard_drive.index(".")

    while free_idx < i:
        value = hard_drive[i]

        if value != ".":
            hard_drive[free_idx] = value
            hard_drive[i] = "."

            if all( [ isinstance(v, int) for v in hard_drive[:i] ] ): break

        i -= 1
        free_idx = hard_drive.index(".")

    print("Part One:", sum( [ file_id * i for i, file_id in enumerate(hard_drive[:hard_drive.index(".")])  ] ))


# Part Two
def partTwo(data) -> None:
    hard_drive = buildHardDrive(data)
    values = [ (val, hard_drive.count(val), [ v for v, ch in enumerate(hard_drive) if ch == val ]) for val in sorted(set([ ch for ch in hard_drive if ch != "." ]), reverse=True) ]

    for file_id, size, positions in values:
        free_idx = findIndex(size, hard_drive)

        if free_idx and free_idx < hard_drive.index(file_id):
            for i in range(free_idx, free_idx + size):
                old_file_idx = positions.pop(0)
                hard_drive[i] = file_id            
                hard_drive[old_file_idx] = "."

    print("Part Two:", sum( [ file_id * i for i, file_id in enumerate(hard_drive)  ] ))


if __name__ == "__main__":
    data = [ int(ch) for line in open("2024/data/Day Eight.txt") for ch in line ]

    partOne(data)
    partTwo(data)
