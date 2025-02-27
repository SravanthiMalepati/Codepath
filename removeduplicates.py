def removeduplicate(li):
    #sorted(li)
    # newli = []
    # for i in sorted(li):
    #     if i not in newli:
    #         newli.append(i)
    # return newli
    # newli = set()
    # #for i in sorted(li):
    # for i in li:
    #     newli.add(i)
    # return newli
    w = 0
    for r in range(0,len(li)):
        if li[r] != li[r-1]:
            li[w] = li[r]
            w +=1
    return li[:w]



print(removeduplicate([1,2,16,6,6,10,14,14]))   