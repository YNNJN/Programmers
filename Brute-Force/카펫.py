def solution(brown, red):
    for a in range(1, int(red**0.5) + 1):
        if not red % a:
             b = red // a #a,b는 가운데 사각형(빨강)의 가로와 세로
             if 2 * a + 2 * b + 4 == brown:
                 return [b+2, a+2]