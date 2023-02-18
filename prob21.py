class prob21():
    i = int(input())
    while i > 0:
        phrase = input()
        word = phrase[0:phrase.index("–")].strip()
        definition = phrase[phrase.index("–") +1:].strip()
        count = 0
        
        if word in definition: 
            print("Perfect")
        else:
            while len(word) > 0 and count < 50:
                span = len(word)
                while span >= 2:
                    if word[0:span] in definition:
                        word = word[span:]
                        span = len(word)
                    else: 
                        span -= 1
                count += 1
            if len(word) == 0:
                print("Perfect")
            else: print("Imperfect!")
            
        i -= 1