import random

random.seed(628824946)

with open('test/input/input01.txt', 'w') as f:
    f.write('123 123\n')

with open('test/input/input02.txt', 'w') as f:
    f.write('123 122\n')

for q in range(3, 11):
    with open('test/input/input%02d.txt' % q, 'w') as f:
        n = random.randint(1, 1000)
        m = random.randint(0, n - 1)
        f.write('%d %d\n' % (n, m))
