import re

max_x = None
max_y = None

# Check to makesure area is in bounds
def inBounds(x, y) -> bool:
    if 0 <= x < max_x and 0 <= y < max_y:
        return True
    else:
        return False


# Build character coordinate list for Part One
def buildCoordinateListP1(a, b) -> list:
    template_list = [
        [( 0, 0), ( 0,-1), ( 0,-2), ( 0,-3)], # Top Verticle
        [( 0, 0), ( 0, 2), ( 0, 2), ( 0, 3)], # Bottom Verticle
        [( 0, 0), ( 1,-1), ( 2,-2), ( 3,-3)], # Top Right Diagonal
        [( 0, 0), ( 1, 0), ( 2, 0), ( 3, 0)], # Right Horizontal
        [( 0, 0), ( 1, 1), ( 2, 2), ( 3, 3)], # Bottom Right Diagonal
        [( 0, 0), (-1,-1), (-2,-2), (-3,-3)], # Top Left Diagonal
        [( 0, 0), (-1, 0), (-2, 0), (-3, 0)], # Left Horizontal
        [( 0, 0), (-1, 1), (-2, 2), (-3, 3)]  # Bottom Left Diagonal
    ]

    return [ [(a - x, b - y) for x, y in template] for template in template_list if all([ inBounds(a - x, b - y) for x, y in template ]) ]


# Build character coordinate list for Part Two
def buildCoordinateListP2(a, b) -> list:
    template_list = [
        [(-1,-1), ( 0, 0), ( 1, 1)], # Top Left To Bottom Right
        [(-1, 1), ( 0, 0), ( 1,-1)]  # Bottom Left to Top Right
    ]

    return [ [(a - x, b - y) for x, y in template] for template in template_list if all([ inBounds(a - x, b - y) for x, y in template ]) ]


# Part One
def partOne(data) -> None:
    ans = 0

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "X":
                coordinates_list = buildCoordinateListP1(x, y)
        
                for word_coordinate_list in coordinates_list:
                    text = "".join( [data[y][x] for x, y in word_coordinate_list] )
            
                    if text == "XMAS" or text == "SAMX":
                        ans += 1

    print("Part One:", ans)


# Part Two
def partTwo(data) -> None:
    ans = 0

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "A":
                words = [ "".join( [data[y][x] for x, y in word_coordinate_list] ) for word_coordinate_list in buildCoordinateListP2(x, y) ]
                check = all([ True if word == "MAS" or word == "SAM" else False for word in words ])
                
                if len(words) == 2 and check:
                    ans += 1

    print("Part Two:", ans)


if __name__ == "__main__":
    data = open("2024/data/Day Four.txt").read().strip().splitlines()
    max_y = len(data)
    max_x = len(data[0])

    partOne(data)
    partTwo(data)