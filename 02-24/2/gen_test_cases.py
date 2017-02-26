#!/bin/python3

import random

LIMIT = 10000

def example_origin():
    start_pos = [0,0]
    elevators = [[1,3],[0,5],[-1,2]]
    closest   = [-1,2]
    return start_pos, elevators, closest

def example_standing_in_elevator():
    start_pos = [0,0]
    elevators = [[0,0]]
    closest   = [0,0]
    return start_pos, elevators, closest

def all_positive():
    start, elevators, closest = example_origin()
    start[0] += 5
    start[1] += 5
    for elevator in elevators:
        elevator[0] += 5
        elevator[1] += 5
    closest[0] += 5
    closest[1] += 5
    return start, elevators, closest

def all_negative():
    start, elevators, closest = example_origin()
    start[0] -= 6
    start[1] -= 6
    for elevator in elevators:
        elevator[0] -= 6
        elevator[1] -= 6
    closest[0] -= 6
    closest[1] -= 6
    return start, elevators, closest

def standing_in_elevator():
    start_pos = [1,-1]
    elevators = [[1,3],[0,5],[-1,2],[1,-1]]
    closest   = [1,-1]
    return start_pos, elevators, closest

def one_elevator():
    start_pos = [-1,-1]
    elevators = [[1,1]]
    closest   = [1,1]
    return start_pos, elevators, closest

def many_elevators():
    start_pos = [-1,1]
    elevators = {(0,1)}
    closest   = [0,1]

    random.seed(0)
    for _ in range(LIMIT):
        neg_x = random.randint(-LIMIT, -3)
        pos_x = random.randint(1, LIMIT)
        x = random.choice([neg_x, pos_x])
        del neg_x, pos_x
        neg_y = random.randint(-LIMIT, -1)
        pos_y = random.randint(2, LIMIT)
        y = random.choice([neg_y, pos_y])
        elevators.add((x,y))

    return start_pos, elevators, closest

def no_elevators():
    start_pos = [-1,-1]
    elevators = []
    closest   = [0,0]
    return start_pos, elevators, closest


TEST_CASE_FNS = [example_origin, example_standing_in_elevator,
                 all_positive, all_negative,
                 standing_in_elevator, one_elevator, many_elevators,
                 no_elevators]

if __name__ == "__main__":
    # Populate test cases
    f_in  = open("test/contest.in", "w")
    f_out = open("test/contest.out", "w")

    f_in.write("{}\n".format(len(TEST_CASE_FNS)))

    for fn in TEST_CASE_FNS:
        start, elevators, closest_elevator = fn()

        # Input is:
        # start coordinate
        # number of elevators
        # location of each elevator.
        f_in.write("{} {}\n".format(start[0], start[1]))
        f_in.write("{}\n".format(len(elevators)))
        for elevator in elevators:
            f_in.write("{} {}\n".format(elevator[0], elevator[1]))

        # Output is:
        # (x,y)
        f_out.write("({},{})\n".format(closest_elevator[0], closest_elevator[1]))

    f_in.close()
    f_out.close()
