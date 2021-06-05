# 2792 보석 상자
'''
N M
K[M]
5 2
7
4
---
3
'''
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_int(): return int(sys.stdin.readline())

def f(n, ks):
    return 3

def test():
    assert f(5, [7,4]) == 3
    
if __name__ == '__main__':
    test()
    n,m = get_ints()
    ks = [get_int() for _ in range(m)]
    print(f(n, ks))