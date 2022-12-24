#1. Définir en Python un tableau d'entiers.
arr=[1,15,24,5,18,54,18,1,6,7,5,18]
#2.calcule la moyenne des nombres contenus dans le tableau donné
def moyenne(x):
    laSomme=sum(x)
    laMoyenne=laSomme//len(x)
    return laMoyenne
print("la moyenne des nombres contenus dans le tableau : ",moyenne(arr))

#3.compte le nombre d'occurrences d'un élément,
def nombre_de_occurrence(x):
    return arr.count(x)

print("le nombre d'occurrences de 18 : ",nombre_de_occurrence(18))
#4.compte combien d'éléments sont supérieurs ou égaux à 10
element=0
for i in arr:
    if i>=10 :
        element+=1
print("le nombre des éléménts supérieur ou égaux à 10 : " ,element)

#5.recherche la valeur maximale du tableau
maxTableau=max(arr)
print("la valeur maximale de tableau : " ,maxTableau)
#6.teste si un élément est présent ou non
n=int(input("entrer un nombre : "))
if n in arr :
    print("le nombre ",n ,"existe au tableau ")
else :
    print("le nombre ", n,"n'existe pas au tableau")

#7.fournit un tableau de n entiers aléatoires
import random
n=int(input("entrer un entier aléatoire : "))
tableau=[]
for i in range(1,n):
    tableau.append(i)
print(tableau)
#8.construit le tableau des n premiers entiers mélangés aléatoirement.
random.shuffle(tableau)
print("tableau mélangés aléatoirement :",tableau)

#9.Sur des grands tableaux, mesurer le temps nécessaire à chacune des fonctions calculant la moyenne et recherchant un élément
import time 
t1 = time.process_time()
print("mesure du temps:  " ,t1,"sec.")