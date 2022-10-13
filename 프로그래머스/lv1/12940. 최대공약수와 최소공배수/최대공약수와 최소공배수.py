def Gcd(n,m):
    if m ==0 :
        return n
    else :
        return Gcd(m, n % m)
    
def solution(n, m):
    return [Gcd(n,m), n*m//Gcd(n,m)]