class prob05():
    num = int(input())
    diction = {}
    for x in range(num):
        n,m,h = input().split()
        score = float(m)/float(h)
        diction[n] = score
    win = min(diction.items(), key=lambda y: y[1])
    print(win[0], win[1])
    