 # 12865 평범한배낭

def f(k, items):
    """Returns the sum of value of all the items in the bag which can take up to K weight.
    
    Parameters
    ----------
    k : int. 버틸 수 있는 최대 무게
    items: [w:int, v:int]: w 각 물건의 무게, v 물건의 가치, 1 <= w <= 100000, 0 <= v <= 1000
    
    Returns
    -------
    value : int. 배낭에 넣은 물건의 가치의 최대 합
    
    Example
    -------
    >>> k = 7
    >>> items = [[6,13], [4,8], [3,6], [5,12]]
    >>> f(k, items)
    14
    """
    print ('items', items)
    c=len(items)
    d=[[0]*(c) for _ in range(k+1)]

    #d[k][ci] 는 k 사이즈에 ci 아이템들을 사용해서 담을수있는최대가치
    for i in range(1, k+1):
        for ci, (w, v) in enumerate(items):
            j=ci-1 if ci-1>=0 else 0
            # not take
            if i-w < 0:
                y = d[i][j]
                y0,y1,y2=-1,-1,-1
            # take maximum 
            else:
                y0 = d[i-1][ci]
                y1 = d[i-w][j] + v
                y2 = d[i][j]
                y = max(y0, y1,y2)
            
            print (f'[{i}][{ci}]', 'y',y, y0, y1, y2)
            d[i][ci] = y
    print ('d', d)
    return d[k][c-1]

assert f(7, [[2, 2], [1, 1], [3, 9]]) == 12
# case 1. take O X X
# case 2. take X O X
# case 3. take X X O
# case 4. take O O X
# case 5. take X O O
# case 6. take O O O
#assert f(7, [[7, 1], [8, 0], [9, 9]]) == 1
assert f(7, [[9, 2], [2, 1], [8, 9]]) == 1
assert f(7, [[9, 3], [9, 2], [6, 1]]) == 1
assert f(7, [[3, 3], [4, 5], [3, 2]]) == 8
assert f(7, [[3, 7], [4, 9], [3, 8]]) == 17
assert f(7, [[2, 2], [1, 1], [3, 9]]) == 12

assert f(7, [
    [6,13],
    [4,8],
    [3,6],
    [5,12]
]) == 14

def get_ints(): return [int(v) for v in input().strip().split()]

if __name__ == '__main__':
    N, K = get_ints()
    items = [get_ints() for _ in range(N)]
    print (f(K, items))
        
def f(k, items):
    """Returns the sum of value of all the items in the bag which can take up to K weight.
    
    Parameters
    ----------
    k : int. 버틸 수 있는 최대 무게
    items: [w:int, v:int]: w 각 물건의 무게, v 물건의 가치, 1 <= w <= 100000, 0 <= v <= 1000
    
    Returns
    -------
    value : int. 배낭에 넣은 물건의 가치의 최대 합
    
    Example
    -------
    >>> k = 7
    >>> items = [[6,13], [4,8], [3,6], [5,12]]
    >>> f(k, items)
    14
    """
    case1 = -1
    
    # 종료 조건
    if items == []: return 0
    
    # 선택을 하는 경우. v 가 k 보다 작아야 함.
    w, v = items[0]
    if w <= k:
        case1 = v + f(k-w, items[1:])
    
    # 선택을 안 하는 경우
    case2 = f(k, items[1:])
    
    ret = max(case1, case2)
    
    return ret
