#1.Implémenter le type abstrait « Pile » vu en cours.
class Pile:
    def __init__(self) -> None:
        self.pile=[]
    
    def push(self,valeur):
        self.pile.append(valeur)
    def vide(self):
        return self.pile==[]
    def pop(self):
        return self.pile.pop()
    def show(self):
        for value in reversed(self.pile):
            print(value)
# ajouter les valeur au pile 
def inserer_valeur_au_pile(p,valeur):
    if p.vide():
        p.push(valeur)
    else:
        popped = p.pop()
        inserer_valeur_au_pile(p, valeur)
        p.push(popped)

#2.Écrire une fonction qui permet d'inverser une pile.
def inversé_pile(p):
    if p.vide():
        pass
    else:
        popped = p.pop()
        inversé_pile(p)
        inserer_valeur_au_pile(p, popped)


pile_=Pile()
pile_.push(1)
pile_.push(2)
pile_.push(3)
pile_.push(4)
pile_.push(5)

print("Original pile :")
pile_.show()
print(" pile inversé :")
inversé_pile(pile_)
pile_.show()
#3.

def expression_verifié(expression):
    pile=[]
    crochet_ouvert=set("([{")
    crochet_fermé=set(")]}")
    pair = {')' : '(' , ']' : '[' , '}' : '{'}
    for i in expression:
        if i in crochet_ouvert:
            pile.append(i)
        elif i in crochet_fermé:
            if not  pile:
                return "l'expression n'est bien parenthésée"
            if pile.pop() !=pair[i]:
                return "l'expression n'est bien parenthésée"
            else:
                continue
    if not pile :
        return "l'expression est bien parenthésée"
    else:
        return "l'expression n'est bien parenthésée"
expression="{[([)]}"
print(expression_verifié(expression))

#4.
x=input("entrée un caractère : ")
def operation_elémentaire(x):
    op=["*","+","-","/"]
    if x in op:
        return "Vrai"
    else:
        return "Faux"
print(" l'opération élémentaire est : ",operation_elémentaire(x))
#une fonction qui prend un symbole-opération et deux entiers et qui renvoie le résultat de l'opération + evaluation 
x=int(input("Donner le premier entier : "))
y=int(input('Donner le deuxiemme entier : '))
op=input("donner le symbole-opération : ")
def operation(x,y,op):
    if op=='+':
        return x+y
    elif op=='-':
        return x-y
    elif op=='*':
        return x*y
    elif op=="/" and y!=0:
        return x/y
    else:
        return "l'opération  est invalide"
print(operation(x,y,op))
#a fonction d'évaluation
def nouvelle_pile():
    return []
def estVide(p):
    return len(p)==0
def empile(x,p):
    p.append(x)

def depile(p):
    return p.pop()

def évaluation(formule):
    p = nouvelle_pile()
    for x in formule :
        if type(x)==int:
            empile(x,p)
        else:
            b=depile(p)
            a=depile(p) 
            empile(operation(b, a,x), p)
    return depile(p)
formule=[3, 4, '+', 6, '****']
print(évaluation(formule))