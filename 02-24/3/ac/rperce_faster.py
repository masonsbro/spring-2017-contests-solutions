T = int(input())
for _ in range(0, T):
    line = input().split(' ')
    height = int(line[0])
    depth  = int(line[1])
    width  = 12 * int(line[2])
    number = int(line[3])

    # If there's, e.g., 5 steps, the total volume is (1 + 2 + 3 + 4 + 5) times that of a
    # single step (+1 makes it inclusive)

    # Then, we know that the sum from 1 to n is (n)(n+1)/2
    step_units = None
    if number % 2 == 0:
        step_units = number // 2 * (number + 1)
    else:
        step_units = (number + 1) // 2 * number

    step_volume = height * width * depth

    print(step_units * step_volume)
