def mergeSortLists(l1, l2):
    l1.sort(); l2.sort()
    print(l1)
    print(l2)
    newlist = []
    for i in range(len(l1)):
        newlist.append(l1[i])
    for j in range(len(l2)):
        newlist.append(l2[j])
    newlist.sort()
    print(newlist)

mergeSortedLists([1,6,7], [2,9,5])