# come funziona il quick sort 
'''

prendiamo un array in considerazione 
arr[0] = pivot --> ma puo essere qualsiasi altra posizione dell'array 

confrontiamo pivot con i numeri maggiori e minori 
cosi da dividere in due parti l'array , da una parte less e dall'altra parte grater

array di tipo ricorsivo 

tempo compiutizzionale
0(n * log n)

Come si imposta
Strategia divide and conquer --> coso <2 elementi restituiamo l'arr
impostiamo pivot
impostiamo less
'''

def quick_sort(arr) : 
    if len(arr) < 2 : 
        return arr
    else : 
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        grater = [i for i in arr[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(grater)
    
arr = [87 , 9 , 1 , 78]
sorted_arr = quick_sort(arr)
print(sorted_arr)

