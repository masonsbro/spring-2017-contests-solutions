from random import randint

MAXN = int(1e5)
MAX = int(1e6)

def sample():
    print("""2
500 3
100 3
3
400 2
600 1
200 3""")

def single():
    print(1)
    speed = randint(int(1e5), MAX)
    dur = randint(int(1e5), MAX)
    print(speed, dur)

def maxvals():
    print(MAXN)
    for _ in range(MAXN):
        print(MAX, MAX)

def main():
    T = 4
    print(T)
    sample()
    single()
    maxvals()


main()
