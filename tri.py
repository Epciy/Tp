import time 
#arr=[1,11,5,47,2,18,54,6]

def tri_insertion(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        
          
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        
        
        arr[j + 1] = key
    temp=time.process_time()
    return temp
#print(tri_insertion(arr))
def tri_extraction(arr):
    size=len(arr)
    for step in range(size):
        min_idx = step
        
        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
         
         

        arr[step], arr[min_idx] = arr[min_idx], arr[step]
    temp=time.process_time()
    return temp
#print(tri_extraction(arr))
def tri_rapide(arr):
    elements = len(arr)
    
    
    if elements < 2:
        return arr
    current_position = 0 
    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp
    
    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp
    
    left =tri_rapide(arr[0:current_position]) 
    right =tri_rapide(arr[current_position+1:elements]) 
    
    arr = left + [arr[current_position]] + right 
    #temp_process=time.process_time()
    
    return arr
def time_tri_rapide(x):
    x
    tmp=time.process_time()
    return tmp

#print(time_tri_rapide(tri_rapide(arr)))
