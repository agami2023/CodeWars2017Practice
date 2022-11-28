class prob04():
    num = int(input())
    for x in range(num):
        m,h = input().split()
        h = float(h)/60
        print(float(m)/h)
        
prob04()