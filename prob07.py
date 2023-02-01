class prob07():
    runs = int(input())
    
    while runs > 0:
        one, A, B, C, M, N, error = input().split()
        one = int(one)
        A = int(A)
        B = int(B)
        C = int(C)
        M = int(M)
        N = int(N)
        error = float(error)
        tries = 0
        
        two = C + ( A * one + M ) / ( B * one + N )
        while (abs(one-two) >= error) and (tries < 100):
            one = two
            two = C + ( A * one + M ) / ( B * one + N )
            if abs(one-two) < error:
                print(two)
            tries = tries + 1  
        if tries >= 100:
            print("DIVERGES")
            
        
        runs = runs - 1
