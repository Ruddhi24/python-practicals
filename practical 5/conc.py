#concatenate two list
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     
# Driver code
list1 = [1, 2, 3,4,5]
list2 = ['p','q']
print(multiplyList(list1))
print(multiplyList(list2))
