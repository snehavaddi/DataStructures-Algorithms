# Python3 Program to find all the
# common characters in n strings
MAX_CHAR = 26


def commonCharacters(strings, n):
    # primary array for common characters
    # we assume all characters are seen before.
    prim = [True] * MAX_CHAR

    # for each strings
    for i in range(n):

        # secondary array for common characters
        # Initially marked false
        sec = [False] * MAX_CHAR

        # for every character of ith strings
        for j in range(len(strings[i])):

            # if character is present in all
            # strings before, mark it.
            if (prim[ord(strings[i][j]) - ord('a')]):
                sec[ord(strings[i][j]) -
                    ord('a')] = True

        # copy whole secondary array
        # into primary
        for i in range(MAX_CHAR):
            prim[i] = sec[i]

        # displaying common characters
    for i in range(26):
        if (prim[i]):
            print("%c " % (i + ord('a')),
                  end="")

        # Driver's Code


strings = ["geeksforgeeks", "gemkstones",
           "acknowledges", "aguelikes"]
n = len(strings)
commonCharacters(strings, n)

# This code is contributed by Niwesh Gupta
