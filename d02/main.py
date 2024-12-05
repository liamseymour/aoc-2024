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

    cum = 0
    for report in reports:
        old_cum = cum
        if not is_gap_less_than_four(report): 
            continue
        cum += is_ascending(report) 
        cum += is_descending(report)

        """
        if cum != old_cum:
            print(f"{report}")
        """

    print(f"PT 1: {cum}")

    # PT 2:

    cum = 0
    for report in reports:
        cum += check_with_dampening(report)


    print(f"PT 2: {cum}")
        
main()
