MAX_CHAR = 26
def commonCharacters(strings, n):
    prim = [True] * MAX_CHAR
    for i in range(n):
        sec = [False] * MAX_CHAR
        for j in range(len(strings[i])):
            print(ord('e'))
            if (prim[ord(strings[i][j]) - ord('a')]):
                sec[ord(strings[i][j]) -
                    ord('a')] = True
        for i in range(MAX_CHAR):
            prim[i] = sec[i]
    for i in range(26):
        if (prim[i]):
            print("%c " % (i + ord('a')),
                  end="")

strings = ["geeksforgeeks", "gemkstones",
           "acknowledges", "aguelikes"]
n = len(strings)
commonCharacters(strings, n)