#1.2.
class Etudiant:
    def __init__(self) -> None:
        self.dictionnaire={}
        self.prenom=''
        self.nom=''
        self.note_informatique=0
        self.note_mathematique=0 
        self.date_naissance=0

    def saisir(self):
        self.prenom=input("saisir le prenom d'étudiant : ")
        self.nom=input("saisir le nom d'étudiant : ")
        self.note_informatique=int(input("entrer la note d'informatique :"))
        self.note_mathematique=int(input("entrer la note de mathématique : "))
        self.date_naissance=int(input(" l'année de naissance : "))

    def afficher(self):
        self.dictionnaire["Nom"]=self.nom
        self.dictionnaire["Prenom"]=self.prenom
        self.dictionnaire["note d'informatique"]=self.note_informatique
        self.dictionnaire["note_mathématique"]=self.note_mathematique
        self.dictionnaire["date_naissance"]=self.date_naissance
        print("Carte d'étudiant {} {} : {}".format(self.nom,self.prenom,self.dictionnaire))
    

etudiant=Etudiant()
etudiant.saisir()
etudiant.afficher()
