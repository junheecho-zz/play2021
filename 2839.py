# 2839 => dynamic programming for avoiding RecursionError

def f(n):
    dp=[-1]*(n+1)
    dp[0]=0
    dp[3]=1
    for i in range(5,n+1):
        c1 = dp[i-3]
        c2 = dp[i-5]
        if c1!=-1 and c2!=-1:
            dp[i]=min(c1,c2)+1
        elif c1!=-1:
            dp[i]=c1+1
        elif c2!=-1:
            dp[i]=c2+1
    return dp[n]

def test():
    assert f(18) == 4
    assert f(4) == -1
    assert f(6) == 2
    assert f(9) == 3
    assert f(11) == 3

if __name__=='__main__':
    test() # ALL PASS
    n = int(input())
    print(f(n))