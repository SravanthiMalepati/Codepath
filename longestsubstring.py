def longestsubstring(s):
    if len(s) == 0:
        return 0
    seen = { }
    currlen = 0
    maxlen = 0
    for index, letter in enumerate(s):
        if letter in seen and seen[letter] >= index - currlen:
            currlen = index - seen[letter]
            seen[letter] = index
        else: # letter is not yet in the dictionary
            seen[letter] = index
            currlen += 1
        print("Letter:", letter, "currlen:", currlen)
        maxlen = max(maxlen, currlen)
    return maxlen

print(longestsubstring("tmmzuxt"))