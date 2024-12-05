def main():
    with open("input") as f:
        lines = f.readlines()
    
    # PT 1

    cumm = -0
    for y, line in enumerate(lines):
        next_x = line.find("X")
        while next_x != -1:
            cumm += check1(lines, next_x, y)

            next_x = line.find("X", next_x+1)

    print(f"PT 1: {cumm}")

    # PT 2

    cumm = -0
    for y, line in enumerate(lines):
        if y == 0 or y == len(lines)-1: continue
        next_x = line.find("A")
        while next_x != -1:
            if next_x != 0 and next_x != len(lines[0])-1:
                cumm += check2(lines, next_x, y)
            next_x = line.find("A", next_x+1)

    print(f"PT 2: {cumm}")

def check1(lines, x, y):
    cumm = 0
    length = len(lines[0])
    height = len(lines)
    if x <= length - 4:
        cumm += lines[y][x+1] == "M" and lines[y][x+2] == "A" and lines[y][x+3] == "S"
    if x >= 3:
        cumm += lines[y][x-1] == "M" and lines[y][x-2] == "A" and lines[y][x-3] == "S"
    if y <= height - 4:
        cumm += lines[y+1][x] == "M" and lines[y+2][x] == "A" and lines[y+3][x] == "S"
    if y >= 3:
        cumm += lines[y-1][x] == "M" and lines[y-2][x] == "A" and lines[y-3][x] == "S"
    if x >= 3 and y >= 3:
        cumm += lines[y-1][x-1] == "M" and lines[y-2][x-2] == "A" and lines[y-3][x-3] == "S"
    if x >= 3 and y <= height - 4:
        cumm += lines[y+1][x-1] == "M" and lines[y+2][x-2] == "A" and lines[y+3][x-3] == "S"
    if x <= length - 4 and y >= 3:
        cumm += lines[y-1][x+1] == "M" and lines[y-2][x+2] == "A" and lines[y-3][x+3] == "S"
    if x <= length - 4 and y <= height - 4:
        cumm += lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S"

    return cumm

def check2(lines, x, y):
    """
    M S S M
     A   A
    M S S M

    M M S S
     A   A
    S S M M
    """
    
    if lines[y-1][x-1] not in "MS": return 0
    if lines[y+1][x-1] not in "MS": return 0
    if lines[y-1][x+1] not in "MS": return 0
    if lines[y+1][x+1] not in "MS": return 0

    if lines[y-1][x-1] == lines[y+1][x+1]: return 0
    if lines[y+1][x-1] == lines[y-1][x+1]: return 0

    return 1



main()
