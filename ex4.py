from restos import liste_restos

# affichage des informations sur un restaurant, à compléter
def affiche_resto (resto):
    print('[',resto.get('pos'),']',end=' ')
    print(resto.get('nom'))
    print()

# boucle sur tous les restaurants, pour affichage
for resto in liste_restos:
    affiche_resto(resto)