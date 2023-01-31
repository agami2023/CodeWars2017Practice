class prob08():
    def decimalToBinary(n):
        return int(bin(n).replace("0b", ""))
    def evenParity(m):
        x = 0
        while m > 0:
            y = m%10
            m = m//10
            x = x + y
        return x
    
    count = 0
    a, b = input().split()
    a = int(a)
    b = int(b)
    A = decimalToBinary(a)
    B = decimalToBinary(b)
    while b >= a:
        if evenParity(B) % 2 == 0:
            count = count + 1
        b = b - 1
        B = decimalToBinary(b)
    
    print(count)
        