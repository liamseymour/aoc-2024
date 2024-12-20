import re


def main():
    with open("input") as f:
        lines = f.readlines()

    # PT 1:

    cumm = 0
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    for line in lines:
        matches = re.findall(mul_pattern, line)
        for match in matches:
            cumm += int(match[0]) * int(match[1])
    print(f"PT 1: {cumm}")

    # PT 2:

    cumm = 0
    mul_pattern = re.compile(r"(mul\((\d+),(\d+)\))|(do\(\)|don't\(\))")
    do = True
    for line in lines:
        matches = re.findall(mul_pattern, line)
        for match in matches:
            if match[3] == "do()":
                do = True
            elif match[3] == "don't()":
                do = False
            elif do:
                cumm += int(match[1]) * int(match[2])
    print(f"PT 2: {cumm}")

main()
