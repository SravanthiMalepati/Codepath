def reverse_string(s1):
    #print(type(s))
    s = list(s1)
    #print(s)
    left = 0
    right = len(s1) - 1
    while left <= right:           
        s[left], s[right] = s[right],s[left]
        left += 1
        right -= 1
    s1 = ''.join(i for i in s)
    return s1


print(reverse_string('example'))      