class prob11():
    rows, cols, noise = input().split()
    rows = int(rows)
    cols = int(cols)
    noise = int(noise)
    words = input().split()
    words = [int(i) for i in words]
    lets = []

    while rows > 0:
        lets = lets + input().split()
        rows = rows - 1
    words = words[1:]
    
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in alpha:
        if lets.count(i) >= noise:
            while lets.count(i) > 0:
                lets.remove(i)

    print(lets)
    phrase = ""
    for i in words:
        while i > 0 and len(lets)>0:
            phrase += lets[0]
            lets = lets[1:]
            i -= 1
        phrase += " "
    print(phrase)