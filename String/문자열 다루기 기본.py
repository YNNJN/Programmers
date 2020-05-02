def isNumber(n):
    try:
        float(int(n))
        return True
    except:
        return False

def solution(s):
    if isNumber(s):
        if len(s) == 4 or len(s) == 6:
            return True
    return False