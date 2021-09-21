def mutilples3ofsand5(n):
    sum = 0
    for i in range(1,n):
        #print(i)
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            i += 1
    return sum

print(mutilples3ofsand5(10))
print(mutilples3ofsand5(1000))