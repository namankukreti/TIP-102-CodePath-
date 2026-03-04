def Goldilocks(arr):
    if 2 >= len(arr):
         return -1
    minnum = min(arr)
    maxnum = max(arr)
    for i in arr:
        if i != minnum and i != maxnum:
            return i


#Test cases
#according to our implementation, the expected result should be the first non min/max value, even though this function could technically return anything.
print(Goldilocks([1, 3, 4, 7, 9]))#3
print(Goldilocks([1, 2]))#-1
print(Goldilocks([2, 1, 3])) #2
print(Goldilocks([])) #-1
print(Goldilocks([5, 6, 7, 9, 20, 3, 4])) #5