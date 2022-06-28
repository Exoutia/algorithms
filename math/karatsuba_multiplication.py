def karatsuba(x: int, y: int):
    if x < 10 or y < 10:
        return x * y
    
    n1 = max(len(str(x)), len(str(y)))
    n2 = n1//2
    
    
    a, b = divmod(x, 10**n2)
    c, d = divmod(y, 10**n2)
    
    m = karatsuba(a, c)
    n = karatsuba(b, d)
    o = karatsuba((a+b), (c+d))
    
    return ((m * 10**(n2*2)) + ((10**n2) * (o - (m + n))) + n)


def main():
    v = karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
    
    print (v)
    
if __name__ == "__main__":
    main()
    
    
    