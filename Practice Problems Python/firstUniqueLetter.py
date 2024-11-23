word = "leetcode"
def uniqueLetter():
    myHash = []
    for c in word:
        if c in myHash:
            myHash[c] += 1
        else:
            myHash[c] = 1
    for c in word:
        if myHash[c] == 1:
            return c