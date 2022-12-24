from collections import defaultdict
#1.
tableau_étudiant=[{"prénom": "Marcel","math":80,"physics":75,"info":95},{"prénom": "Natacha","math":80,"physics":95,"info":55},{"prénom": "réne","math":60,"physics":40,"info":65},{"prénom": "robert","math":50,"physics":85,"info":60}]


#2.implémenter la fonction moyenne d'un étudiant dédiée cette représentation
def moyenne(x):
    res=[]
    for etudiant in x :
        moyenne=(etudiant["physics"]+etudiant["math"]+etudiant["info"])//3
        res.append((etudiant['prénom'],moyenne))
    return res
print("la moyenne de chaque étudiant: ",moyenne(tableau_étudiant))
#3.pour chaque discipline, la fonction moyenne de la promotion
def moyenne_discipline(x):
    dictt=defaultdict(int)
    for etudiant in x:
        dictt["physics"]+=etudiant['physics']
        dictt["math"]+=etudiant["math"]
        dictt["info"]+=etudiant["info"]
    
    for key,value in dictt.items():
        dictt[key]=value//len(x)
    return dictt

print("la note moyenne de chaque discipline : ",moyenne_discipline(tableau_étudiant))


#la fonction qui trouve l'étudiant ayant eu la note moyenne maximale,
def max_moyenne(y):
    y=sorted(y,key=lambda x: x[1], reverse=True)
    return y[0][0]
moyenne_etudiant=moyenne(tableau_étudiant)
print("l'étudiant ayant la note moyenne maximale: ",max_moyenne(moyenne_etudiant))