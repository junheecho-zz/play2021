import sys
import math

def f(n, ms):
    all_jewels = sum(ms)
    minimum_jewels = all_jewels // n
    ns = []
    '''
    5 * (7/11) = 3.xx
    5 * (4/11) = 1.xx
    7 / 3 = 2.33 (+1) => 3
    4 / 2 = 2 
    '''
    for k in ms:
        assigned_people = math.floor(n * (k / all_jewels))
        if assigned_people < 1:
            assigned_people = 1 
        maximum_jewels_per_person = math.ceil(k / assigned_people)
        ns += [maximum_jewels_per_person]
    print(ns)
    return max(ns)

def test():
    # 3.18, 1.81
    # [2,2,3], [2,2]
    
    assert f(5, [7,4]) == 3
    
    # 4.54, 0.45
    # [3,3,2,2], [1]
    assert f(5, [10,1]) == 3

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_int(): return int(sys.stdin.readline())
    
if __name__ == '__main__':
    test()
    n,m = get_ints()
    ks = [get_int() for _ in range(m)]
    print(f(n, ks))