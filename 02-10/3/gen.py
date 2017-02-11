import random

random.seed(164572)

print 100
for q in range(100):
    n = random.randint(1, 1000)
    print n
    s = set()
    while len(s) < n:
        s.add(random.randint(1, 1000000000))
    print ' '.join(map(str, list(s)))
