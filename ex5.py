#1.Implémenter une fonction index_minimum(t,d,f) qui renvoie le numéro de la case contenant la plus petite valeur du tableau t entre les cases d et f.
def index_minimum(t,d,f):
    minimun=min(t[d:f+1])

    return t.index(minimun)


t=[1,8,7,9,4,3,18,10,15]

d,f=3,9
print("le numéro de la case contenant la plus petite valeur du tableau t: ",index_minimum(t,d,f))

#2.Programmer un tri à bulles.
def bubbleSort(t):
    for i in range(len(t)):
        for j in range(0, len(t) - i - 1):
            if t[j] > t[j + 1]:
                temp = t[j]
                t[j] = t[j+1]
                t[j+1] = temp
    return t


print('tableau trié :',bubbleSort(t))
#Sur les tableaux déjà triés
#1.Implémenter une fonction de recherche d'un élément utilisant une boucle tant que et tirant parti du fait que les éléments sont ordonnés.
def recherche(t,element):
    while t[0]<=element<=t[-1]:
        if element in t:
            return "l'element "+ str(element) +" existe dans le tableau "
    # si l'element n'existe pas dans le tableau t .
    return -1
print(recherche(t,7)) 
#2.une fonction de recherche dichotomique.
low=0
high=len(t)-1

def recherche_dichotomique(t,low,high,target):
    if high >= low:
        mid=(low+high)//2
        if t[mid]==target:
            return mid
        elif t[mid]>target:
            return recherche_dichotomique(t,low,mid-1,target)
        else:
            return recherche_dichotomique(t,mid+1,high,target)
    return -1
target=8
print("le nombre de la case de target : ",recherche_dichotomique(t,low,high,target))

#3.une procédure insertion(e,t,n) qui ajoute un élément e à sa place dans un tableau t de taille n
def insertion(e,t,n):
    t.insert(n,e)
    return t
print("insertion de nombre 22 a la 4 eme place :",insertion(22,t,4))

#Autres méthodes de tri
#1.
def tri_extraction(arr):# selction sort()
    size=len(arr)
    min_idx =index_minimum(arr,0,size)
    for step in range(size):
        
        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
         

        arr[step], arr[min_idx] = arr[min_idx], arr[step]
    
    return arr


tab = [111, 34, 22, 55, 4, 2, 1, 77]
print(" tableau aprés tri extraction: ",tri_extraction(tab))

#2.
def tri_insertion(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        
          
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            
            j = j - 1
        
        
        arr[j + 1] = key
        
    
    return arr
print(tri_insertion(tab))