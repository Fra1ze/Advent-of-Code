# Cycle through the list of directions
def changeDirection(direction):
    next_direction_idx = (directions.index(direction) + 1) % len(directions)
    return directions[next_direction_idx]


# Check if obstruction could cause infinite loop
def simulatePath(loc, data):
    if data[loc[0]][loc[1]] == "^":
        return False

    data = [ tuple([ ch if (x, y) != loc or ch == "^" else "#" for x, ch in enumerate(row)]) for y, row in enumerate(data) ]
    in_Bounds = True
    pos = [ (x, y) for x in range(max_x) for y in range(max_y) if data[y][x] == "^" ][0]
    direction = "^"
    history = list()

    while in_Bounds:
        same_direction = True
        ox, oy = movements[directions.index(direction)]

        while same_direction:
            x, y = pos

            if 0 <= x + ox < max_x and 0 <= y + oy < max_y:
                if data[y + oy][x + ox] == "#":
                    if (direction, pos) in history:
                        return True
                    
                    history.append((direction, pos))
                    direction = changeDirection(direction)
                    same_direction = False
                
                else:
                    if 0 <= x + ox < max_x and 0 <= y + oy < max_y:
                        pos = (x + ox, y + oy)

            else:
                in_Bounds = same_direction = False

    return False


# Contains Part One and Part Two
def main(data) -> None:
    in_Bounds = True
    pos = [ (x, y) for x in range(max_x) for y in range(max_y) if data[y][x] == "^" ][0]
    direction = "^"
    visted = set([pos])
    
    while in_Bounds:
        ox, oy = movements[directions.index(direction)]
        x, y = pos
        
        if 0 <= x + ox < max_x and 0 <= y + oy < max_y:
        
            if data[y + oy][x + ox] == "#":
                direction = changeDirection(direction)
            
            else:
                if 0 <= x + ox < max_x and 0 <= y + oy < max_y:
                    visted.add((x + ox, y + oy))
                    pos = (x + ox, y + oy)

        else:
            in_Bounds = False

    print("Part One:", len(visted))
    print("Part Two:", len([ loc for loc in visted if simulatePath(loc, data) ]))


if __name__ == "__main__":
    global max_x, max_y, directions, movements

    data = [ [ ch for ch in row ] for row in open("2024/data/Day Six.txt").read().strip().splitlines() ]
    max_x, max_y = len(data[0]), len(data)
    directions = ["^",">","v","<"]
    movements = [(0,-1),(1,0),(0,1),(-1,0)]

    main(data)