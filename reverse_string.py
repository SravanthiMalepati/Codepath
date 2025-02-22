def reverse_string(s):
    print(type(s))
    s = list(s)
    print(s)
    left = 0
    right = len(s) - 1
    while left <= right:           
        s[left], s[right] = s[right],s[left]
        left += 1
        right -= 1
    s = ''.join(i for i in s)
    return s


print(reverse_string('example'))      