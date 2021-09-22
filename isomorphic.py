def isIsomorphic(s, t):
    #Understand
    #Match hashmap question
    #I will use a hashmap that has the key of letter and the value of a array with the indexes that letter appears
    #I can then compare all keys and their arrays
    #Plan
    sMap = {}
    tMap = {}        
    for c1, c2 in zip(s, t):
        print("c1", c1)
        print("c2", c2)
        if (c1 not in sMap) and (c2 not in tMap):
            sMap[c1] = c2
            tMap[c2] = c1
        elif sMap.get(c1) != c2 or tMap.get(c2) != c1:
            return False
    return True
print(isIsomorphic("foo","bar"))
print(isIsomorphic("mom","dad"))
print(isIsomorphic("test","boo"))
print(isIsomorphic("mop","dad"))