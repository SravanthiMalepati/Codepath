def substring(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    if len2 > len1: return False
    # for i,char in enumerate(string1):
    #     if char == string2[0]:
    #         return True
    #     elif string2 == string1[i:i+len2:]:
    #         return False
    for i,char in enumerate(string1):
        if char == string2[0]:
            if i + len(string2) > len(string1):
                return False
            if string2 == string1[i: i+len(string2)]:
                return True
    return False
    # if cmp == string2:
    #     return True
    # else:
    #     return False
string1 = 'bananas'
string2 = 'nas'
print(substring(string1,string2))
print(substring('laboratory', 'rat'))
print(substring('cat', 'meow'))