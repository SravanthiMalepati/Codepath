def removeduplicate(li):
    #sorted(li)
    # newli = []
    # for i in sorted(li):
    #     if i not in newli:
    #         newli.append(i)
    # return newli
    newli = set()
    #for i in sorted(li):
    for i in li:
        newli.add(i)
    return newli



print(removeduplicate([1,2,16,6,6,10,14,14]))   