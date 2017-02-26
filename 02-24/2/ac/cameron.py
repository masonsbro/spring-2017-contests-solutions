t = int(input())
def manhattan_distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for i in range(t):
    x,y = map(int, input().split())
    elevators = int(input())
    min_coord = (0,0)
    min_distance = 10001
    for j in range(elevators):
        e_x, e_y = map(int, input().split())
        distance = manhattan_distance((e_x, e_y), (x,y))
        if distance < min_distance:
            min_coord = (e_x, e_y)
            min_distance = distance
    print("("+str(min_coord[0])+","+str(min_coord[1])+")")