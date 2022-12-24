#1.Tester l'instruction d'affichage print de Python
number=int(input("entrer un nombre : "))
string=str(input("entrer une chaîne de caractères : "))
variable=input("Declarer une variable : ")
print(number,"\n",string,"\n",variable)


#2. on ajoute "\n "  aprés chaque variable pour passer a la ligne 
#meme ligne end=" "

#3. la boucle while 
n=0
while n<=100 :
    print( " n=  ",n)
    n+=1

#la Boucle For 
for i in range(101):
    print("i= ",i)

#4. Les figures Geometrique 
#triangle non creux :
n =5
for i in range(1, n+1):
      print(' ' * n, end='')
      print('* '*(i))
      n -= 1
# traingle creux :

r=12
for i in range(r):
    for j in range(r-i):
        print(' ', end='') 
    
    for j in range(2*i+1):
        if j==0 or j==2*i or i==r-1:
            print('*',end='')
        else:
            print(' ', end='')
    print() 
# carré  non creux :

c= 4

for i in range(c):
    for j in range(c):
        print('-' , end=' ')
    print()

# creux carré :
k=6
i = 0
while(i < k):
    j = 0
    while(j < k):
        if(i == 0 or i == k - 1 or j == 0 or j == k - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
        j = j + 1
    i = i + 1
    print()


#5.Lists
liste_vide=[]
liste_non_vide=[1,8,7,2,4,6,15,9]
#6.la longueur de liste
print("la longueur de liste : ",len(liste_non_vide))
# 7. enlever une case
liste_non_vide.remove(8)
print("affichage de liste aprés l'enlevement d'une case : ",liste_non_vide)
#ajouter une autre case 
liste_non_vide.append(20) 
print("nouveau liste on ajoutant une autre case : ",liste_non_vide)
#8.parcourir les éléments de la liste et les afficher un par un en utilisant la boucle 
for num in liste_non_vide:
    print(num)
# une autre possibilité
for i in range(len(liste_non_vide)):
    print(liste_non_vide[i]) 

#9.Aléatoire en Python

import random
print( "un entier entre 5 et 20: ",random.randint(5,20))
print("entier pair entre 10 et 98: ",random.randrange(10,100,2)) 
print("un élément dans la liste_non_vide au hasard : ",random.choice(liste_non_vide))
print("afficher la liste non vide avant le mélange aléatoire :",liste_non_vide)
random.shuffle(liste_non_vide)    # mélange aléatoire
print("afficher la liste non vide aprés le mélange aléatoire : ",liste_non_vide)

