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
    v = karatsuba(123458, 5678)
    
    print (v==(123458*5678))
    
if __name__ == "__main__":
    main()
    
    
    