m = 2;
n = 5;


def sum(m, n):
    result = m
    if n<0:
        for _ in range(abs(n)):
            result -= 1
        return result
    else:
        for _ in range(n):
            result += 1
        return result


def divide(m,n):
    
    if n == 0:
        raise ZeroDivisionError
    
    result = 0
    negativeResult = m>0 and n<0 or m<0 and n>0
    n= abs(n)
    m= abs(m)
   
    while(m-n >= 0):
        m -= n
        result+=1

    result = -result if negativeResult else result

    return result