def happynumber(n):
    newNum = 0 
    if n == 1 or n == 7: 
        return True
    elif n < 10: 
        return False
    else:
        while n > 0:
            newNum += pow(n%10,2)
            n = n//10
        print(n, newNum)
    return happynumber(newNum)

print(happynumber(19))
print(happynumber(2))