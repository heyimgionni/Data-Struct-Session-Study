def findSmallest(arr) : 
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1 , len(arr)) : 
        if arr[i] < smallest : 
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr) : 
    newArr = []
    while arr :  # continua fino alla fine dell'array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

lst = [8,5,4,9,1]
print(selection_sort(lst))