from random import randint

def gen_small():
    S = randint(1, 1e2)
    T = randint(1, 1e4)
    C = list(map(lambda x: randint(1, 1e2), range(S)))
    print(S, T)
    print(' '.join(map(str, C)))

def gen_medium():
    S = randint(1, 1e3)
    T = randint(1, 1e6)
    C = list(map(lambda x: randint(1, 1e4), range(S)))
    print(S, T)
    print(' '.join(map(str, C)))

def gen_large():
    S = randint(1, 1e5)
    T = randint(1, 1e9)
    C = list(map(lambda x: randint(1, 1e6), range(S)))
    print(S, T)
    print(' '.join(map(str, C)))

def main():
    gen_large()

main()
