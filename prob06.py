class prob06():
    arrays = int(input())
    
    while arrays > 0:
        num = input().split()
        num.pop(0)
        diffs = []
        i = 0
        while i < len(num)-1:
            diffs.append(int(num[i+1])-int(num[i]))
            i = i+1
        a = 0
        while a < len(diffs):
            diffs[a] = diffs[a]*-1
            a = a + 1
        result = []
        result.append(int(num[0]))
        e = 0
        while e < len(diffs):
            result.append(result[e]+diffs[e])
            e = e + 1
        print(result)
        arrays = arrays - 1