import sys

def f(n, ms):
    # ms is sorted by ascending order
    ms.sort()
    while len(ms) < n:
        max_jewel = ms[-1]
        if max_jewel == 1: break
        h0 = max_jewel//2
        h1 = max_jewel - h0
        del ms[-1]
        for v in [h0,h1]:
            i = binary_search(ms, v)
            ms.insert(i, v)

    return max(ms)

def binary_search(ms, v):
    n = len(ms)
    i = n // 2
    while i < n and i >= 0:
        m1 = ms[i]
        if v > m1:
            i = (i+1+n) // 2
            continue
        m0 = ms[i-1] if i > 0 else v
        if v >= m0 and v <=m1:
            break
        if v > m1:
            i = (i + n) // 2
        elif v <= m1:
            i = i // 2
    return i

assert binary_search([1], 5) == 1
assert binary_search([1,2,3,4], 3) == 2
assert binary_search([1,2,3,4], 2) == 2
assert binary_search([1,2,3,4], 1) == 1
assert binary_search([1,2,3,4], 0) == 0

assert f(5, [7,4]) == 3
assert f(5, [10,1]) == 3

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_int(): return int(sys.stdin.readline())

def time_check(counts):
    import random
    import time

    for i in range(counts):
        n = random.randint(10**3, 10**5)

        jewels = [random.randint(1, 300000) for _ in range(n//2)]
        print ('|jewels| =', n)
        start = time.time()
        r = f(n, jewels)
        elap = time.time()-start
        print ('len', len(jewels), 'time', elap, 'ret',r)

if __name__ == '__main__':
    time_check(10)
    n,m = get_ints()
    ks = [get_int() for _ in range(m)]
    print(f(n, ks))


