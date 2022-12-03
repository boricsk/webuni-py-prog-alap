def array_diff(a, b):
    #your code here
    returnList = []
    for item in a:
        if item != b[0]:
            returnList.append(item)
    return returnList
    
print(array_diff([1,2,2,3,2,2,4,4,7,8,7,6],[2]))

    # elif a.count(b[0]) > 1:
    #     returnValue = set(a)
    #     returnValue.remove(b[0])
    #     return list(returnValue)
    # else:
    #     returnValue1 = a.remove(b[0])
    #     #returnValue.remove(b[0])
    #     return returnValue1