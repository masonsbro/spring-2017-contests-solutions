import random

random.seed(272513235)

for q in range(11, 21):
    with open('test/input/input%d.txt' % q, 'w') as f:
        n = random.randint(1001, 1000000)
        m = random.randint(0, n - 1)
        f.write('%d %d\n' % (n, m))
