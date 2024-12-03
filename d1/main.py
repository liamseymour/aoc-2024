
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

    cum = 0
    for l, r in zip(left, right):
        cum += abs(l-r)

    print(f"Pt 1: {cum}")


    # PT 2:

    r_counts = {}

    for n in right:
        if not n in r_counts:
            r_counts[n] = 1
        else:
            r_counts[n] += 1

    cum = 0
    for n in left:
        if n in r_counts:
            cum += n*r_counts[n]

    print(f"Pt 2: {cum}")


    

main()

