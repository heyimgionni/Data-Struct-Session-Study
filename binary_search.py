# best case 0(1) average case 0(log n)

def binary_search(list , item) : # passiamo alla funzione l'array da cui cercare , e cosa cercare 
    low = 0 #inizio lista index 0
    high = len(list) - 1 # fine lista index - 1 

    while low <= high : 
        mid = (low + high) // 2 # con il binary search inziamo a controllare dal mezza e poi buttiamo quello che non ci serve
        if list[mid] == item : 
            return mid
        if list[mid] > item : 
            high = mid - 1
        else : 
            low = mid + 1
    return None #quando item non è in lista 

# la lista che passiamo deve essere ordinata 

lst = [1 , 6 , 9 , 45 , 98]
print(binary_search(lst , 6))