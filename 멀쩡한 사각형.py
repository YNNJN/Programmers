#GCD를 이렇게도 구현할 수 있다!

def gcd(n,m):
    while m:
        n,m = m, n % m
    return n

def solution(w,h):
    l = gcd(w,h)
    return w*h -l*((w//l)+(h//l)-1)