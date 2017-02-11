import fileinput

lines = fileinput.input()

num_tests = int(lines.readline())
for _ in range(num_tests):
    total_spd = 0
    total_hrs = 0

    num_speeds = int(lines.readline())
    for _ in range(num_speeds):
        spd, hrs = (int(x) for x in lines.readline().strip().split())
        total_spd += hrs * spd
        total_hrs += hrs

    print(round(total_spd / total_hrs))
