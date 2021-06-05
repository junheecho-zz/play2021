# 1463. 1로 만들기
def f(n):
    dp = [0]*(n+1)
    dp[1] = 0
    for i in range(2,n+1):
        vs = []
        if i%3==0:
            vs.append(dp[i//3] + 1)
        if i%2==0:
            vs.append(dp[i//2] + 1)
        
        vs.append(dp[i-1]+1)

        dp[i] = min(vs)

    return dp[n]

def test():
    assert f(2)==1, f(2)
    assert f(10)==3

if __name__ == '__main__':
    test()
    n=int(input())
    print(f(n))

# recursive version
def f(n):
    return g(n,0)

def g(n,acc):
    if n==1: return acc

    rs = []
    if n%3 == 0:
        rs += [g(n/3, acc+1)]
    if n%2 == 0:
        rs += [g(n/2, acc+1)]
    
    if n > 1:
        rs += [g(n-1, acc+1)]
    
    return min(rs)
