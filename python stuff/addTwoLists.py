result = []
def addTwoLists(list1, list2):
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    print(result)

addTwoLists([1,1,1], [1,1,1])