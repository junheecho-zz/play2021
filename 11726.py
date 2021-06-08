# 11726. 2xn 타일링
def f(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]%10007
    
assert f(2) == 2
assert f(9) == 55

if __name__ == '__main__':
    n = int(input())
    print (f(n))