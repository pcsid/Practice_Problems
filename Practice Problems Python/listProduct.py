list = [1,2,3,4,5]
def listProduct(list):
    returnList = [1] * len(list)
    left = 1
    right = 1
    for i in range(len(list)):
        returnList[i] *= left
        left *= list[i]
    for i in range(len(list)-1, -1, -1):
        returnList[i] *= right
        right *= list[i]
    return returnList

#we want to iterate through lkst, multiplying everything around index we currently on by value of the index - O(N) complexity