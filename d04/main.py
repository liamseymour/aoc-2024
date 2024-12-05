def main():
    with open("input") as f:
        lines = f.readlines()
    
    cumm = -0
    for y, line in enumerate(lines):
        next_x = line.find("X")
        while next_x != -1:
            cum += check(next_x, y)

            next_x = line.find("X", next_x+1)

def check(lines, x, y):
    cumm = 0
    if x <= len(lines[0]) - 4:
        


main()
