def isValid(s):
    Parantheses = {')':'(','}':'{',']':'['}
    # print(type(Parantheses))
    empty_stack = []
    for char in s:
        if char in Parantheses:
            if not empty_stack or empty_stack.pop() != Parantheses[char]:    
                return False
        else:
            empty_stack.append(char)
    return not empty_stack

print(isValid("[}{]")) #False
print(isValid("[]")) #True