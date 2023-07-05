
def fibonnaciLooped(n):
    first,second = 0,1
    if n == 0 :
        return 0
    elif n == 1:
        return  1
    else:
        for i in range(n):
            fib = first + second
            first = second
            second = fib
    return fib


def recursiveFibonnaci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFibonnaci(n-1) + recursiveFibonnaci(n-2)
        # a = recursiveFibonnaci(n-1)
        # b = recursiveFibonnaci(n-2)
        # return a + b


if __name__ == '__main__':
    print(fibonnaciLooped(14))

    print(recursiveFibonnaci(14))