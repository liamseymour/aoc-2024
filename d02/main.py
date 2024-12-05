def is_ascending(report):
    for i in range(len(report)-1):
        if report[i] >= report[i+1]: return 0
    return 1
def is_descending(report):
    for i in range(len(report)-1):
        if report[i] <= report[i+1]: return 0
    return 1
def is_gap_less_than_four(report):
    for i in range(len(report)-1):
        if abs(report[i] - report[i+1]) > 3: return 0
    return 1

def check_with_dampening(report):
    for i in range(len(report)):
        removed = report[:i] + report[i+1:]
        
        if not is_gap_less_than_four(removed):
            continue

        if is_descending(removed) or is_ascending(removed):
            return True
        
    return False


def main():
    with open("input") as f:
        inp = f.read()
    
    reports = []

    for l in inp.splitlines():
        reports.append([int(s) for s in l.split()])

    # PT 1:

    cumm = 0
    for report in reports:
        old_cumm = cumm
        if not is_gap_less_than_four(report): 
            continue
        cumm += is_ascending(report) 
        cumm += is_descending(report)

        """
        if cumm != old_cumm:
            print(f"{report}")
        """

    print(f"PT 1: {cumm}")

    # PT 2:

    cumm = 0
    for report in reports:
        cumm += check_with_dampening(report)


    print(f"PT 2: {cumm}")
        
main()
