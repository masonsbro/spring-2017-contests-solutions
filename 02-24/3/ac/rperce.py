T = int(input())
for _ in range(0, T):
    line = input().split(' ')
    height = int(line[0])
    depth  = int(line[1])
    width  = 12 * int(line[2])
    number = int(line[3])

    # If there's, e.g., 5 steps, the total volume is (1 + 2 + 3 + 4 + 5) times that of a
    # single step (+1 makes it inclusive)
    step_units = sum(range(0, number+1))

    step_volume = height * width * depth

    print(step_units * step_volume)
