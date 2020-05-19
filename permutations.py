def P(n,m):
    if n >= m :
        ans = 1
        for i in range(m) :
            ans *= n - i 
        return ans
    else:
        return 0 

def C(n,m):
    if n >= m :
        ans = 1
        for i in range(m) :
            ans *= (n - i) / (i + 1)
        return int(ans)
    else :
        return 0