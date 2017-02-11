from random import randrange
t = 10
print(t)
for i in range(t):
    n = 10000
    m = randrange(500,1000)
    print(str(n) + " " + str(m))
    for j in range(n):
        print(str(randrange(1,100)) + " ",end="")
    print()