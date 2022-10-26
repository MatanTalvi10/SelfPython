import string


def sumdigits(num:int) -> int:
    assert int(num) == num and num >= 0, 'please enter a positive integer'
    if len(str(num)) == 1:
        return num
    else:
        return num%10 + sumdigits(num//10)

def numPower(base: int,exp: int) -> int:
    assert int(exp) == exp, 'please enter a legal integer'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/numPower(base,(-1)*exp)
    else:
        return base * numPower(base,exp-1)

def decToBin(n: int) -> int:
    assert int(n) == n, 'please enter a legal integer'
    if n in [0,1]:
        return string(n)
    else:
    