import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def get_int(): return int(sys.stdin.readline())

def f(ns):
    def f_(ns, prohibited):
        if ns == []: return 0
        rgb = ns[0]
        vs = []
        for i, c in enumerate(rgb):
            if i != prohibited:
                vs += [c + f_(ns[1:], i)]
        return min(vs)
    return f_(ns, -1)
# overlapping sub-optimal?
def f(ns):
    count = len(ns)
    dp = [0] * (1 + count)
    dp[0] = min(ns[0])
    for i in range(1, count):
        dp[i] = dp[0] + min(ns[i])


    return dp[len(ns)]

assert f([
    [26,40,83], 
    [49,60,57], 
    [13,89,99]]) == 96

if __name__ == '__main__':
    n = get_int()
    ns = [get_ints() for _ in range(n)]
    print (f(ns))