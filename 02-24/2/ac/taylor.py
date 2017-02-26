import fileinput

lines = fileinput.input()
num_tests = int(lines.readline())

for _ in range(num_tests):
    me = tuple(map(int, lines.readline().split()))

    num_elevators = int(lines.readline())
    if num_elevators == 0:
        print("(0,0)")
        continue
    elif num_elevators == 1:
        x,y = map(int, lines.readline().split())
        print("({},{})".format(x,y))
        continue
    else:
        num_elevators -= 1
        x,y = map(int, lines.readline().split())
        best_elevator = [x,y]
        best_elevator.append(abs(me[0] - best_elevator[0]) + abs(me[1] - best_elevator[1]))

    for _ in range(num_elevators):
        x,y = map(int, lines.readline().split())
        new_distance = abs(me[0] - x) + abs(me[1] - y)
        if new_distance < best_elevator[2]:
            best_elevator = [x,y,new_distance]

    print("({},{})".format(best_elevator[0], best_elevator[1]))
