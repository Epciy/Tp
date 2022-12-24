#1.2.
N=int(input("donner une valur N: "))
u=N
arr=[N]
T=0
Z=0
while u!=1:
    if u%2==0:
        u=u//2
    else:
        u=(u*3+1)
    arr.append(u)
    T+=1
   
    Z=max(arr)

print("trajectoire: ",arr)
print(" durée de vol : ",T)
print(" altitude maximale : ",Z)

#3.Écrire une fonction qui permet de tester la conjecture pour un entier donné et qui renvoie sa carte d'identité renseignée

def  syracuse(N):
    u=N
    T=0
    L=[N]
    while u!=1:
        if u%2==0:
            u=u//2
        else:
            u=(u*3+1)
        L.append(u)
        T+=1
    Z=max(L)
    carte={"trajectoire":L,
    "durée_de_vol":T,
    "altitude_maximale":Z
    }
   
    return carte 
print(syracuse(N))

#4.Écrire ensuite une fonction qui teste tous les entiers dans un intervalle donné et renvoie toutes les cartes d'identité de ces entiers.
x0,y0=90,120
cartes=[]
def ensemble_des_carte(x0,y0):
    for i in range(x0,y0+1):
        if i%2==0:
            cartes.append(syracuse(i))
    return cartes
print("les cartes d'identité de des entiers  a l'intervalle [90,120]:  ",ensemble_des_carte(x0,y0))   

#5.Utiliser cette fonction pour afficher les cartes présentant une durée de vol strictement supérieure à 100.
resultat=[]
def duree_sup(cartes):
    for carte in cartes:
        if carte["durée_de_vol"]>100:
            resultat.append(carte)
    return resultat

print("les cartes présentant une durée de vol strictement supérieure à 100 :  ",duree_sup(cartes))

#6.Implémenter un tri à bulles pour classer des cartes par altitude décroissante.
altitude=[]
for carte in cartes :
    altitude.append(carte["altitude_maximale"])
print("alt :" ,altitude)
def bubble_sort(altitude):
    for passesLeft in range(len(altitude)-1, 0, -1):
        for i in range(passesLeft):
            if altitude[i] < altitude[i + 1]:
                    altitude[i], altitude[i + 1] = altitude[i + 1], altitude[i]
    return altitude
print("alt reverse :",bubble_sort(altitude))