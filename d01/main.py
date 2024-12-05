
def main():
    with open("input") as f:
        inp = f.read()
    
    left, right = [], []
    for line in inp.splitlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    # PT 1:

    left.sort()
    right.sort()

    cumm = 0
    for l, r in zip(left, right):
        cumm += abs(l-r)

    print(f"Pt 1: {cumm}")


    # PT 2:

    r_counts = {}

    for n in right:
        if not n in r_counts:
            r_counts[n] = 1
        else:
            r_counts[n] += 1

    cumm = 0
    for n in left:
        if n in r_counts:
            cumm += n*r_counts[n]

    print(f"Pt 2: {cumm}")


    

main()

