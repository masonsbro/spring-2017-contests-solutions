import random

MAX_N = 100000
MAX_M = 100000
INPUT_STEM = 'test/input/input'
OUTPUT_STEM = 'test/output/output'
NUM_RAND_NO = 12
NUM_RAND_YES = 12

random.seed(263135)

def make_input(f, g):
    f.write('%d %d\n%s\n' %
            (g[0], g[1], '\n'.join(map(lambda p: ' '.join(map(str, p)), g[2]))))

def make_output(f, ans):
    f.write('%s\n' % ans)

def gen_sample_1():
    return (4, 4, [(1, 2), (2, 3), (3, 4), (4, 2)]), 'YES'

def gen_sample_2():
    return (4, 4, [(1, 2), (1, 3), (2, 3), (3, 4)]), 'NO'

def gen_chain():
    n = MAX_N
    m = n - 1
    edges = [(i, i + 1) for i in range(1, n)]
    return (n, m, edges), 'NO'

def gen_cycle():
    n = MAX_N
    m = MAX_N
    edges = [(i + 1, (i + 1) % n + 1) for i in range(n)]
    return (n, m, edges), 'YES'

def gen_disconnected_no():
    return (4, 2, [(1, 2), (3, 4)]), 'NO'

def gen_disconnected_yes():
    return (3, 2, [(2, 3), (3, 2)]), 'YES'

def gen_random_no():
    n = random.randint(MAX_N / 2, MAX_N)
    m = random.randint(MAX_M / 2, MAX_M)
    perm = list(range(1, n + 1))
    random.shuffle(perm)
    edges = set()
    for i in range(m):
        u = random.randint(0, n - 2)
        v = random.randint(u + 1, n - 1)
        edges.add((perm[u], perm[v]))
    edges = list(edges)
    m = len(edges)
    return (n, m, edges), 'NO'

def gen_random_yes():
    n = random.randint(MAX_N / 2, MAX_N)
    cycle_len = random.randint(2, n)
    m = random.randint(max(cycle_len, MAX_M / 2), MAX_M)
    perm = list(range(1, n + 1))
    random.shuffle(perm)
    edges = set()
    for i in range(cycle_len):
        edges.add((perm[i], perm[(i + 1) % cycle_len]))
    for i in range(m - cycle_len):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u == v: continue
        edges.add((perm[u], perm[v]))
    edges = list(edges)
    m = len(edges)
    return (n, m, edges), 'YES'

det_gen = [gen_sample_1, gen_sample_2, gen_chain, gen_cycle,
           gen_disconnected_no, gen_disconnected_yes]

rand_gen = [gen_random_no] * NUM_RAND_NO + [gen_random_yes] * NUM_RAND_NO
random.shuffle(rand_gen)

gen_all = det_gen + rand_gen

for i, gen in enumerate(gen_all):
    with open(INPUT_STEM + '%02d.txt' % i, 'w') as f_in, \
            open(OUTPUT_STEM + '%02d.txt' % i, 'w') as f_out:
        g, ans = gen()
        make_input(f_in, g)
        make_output(f_out, ans)
