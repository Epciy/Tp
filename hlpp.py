def nouvelle_pile():
    return []
def estVide(p):
    return len(p)==0
def empile(x,p):
    p.append(x)

def depile(p):
    return p.pop()


def applique(o,a,b):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
    elif o=="/":
        return a/b

def évaluation(formule):
    p = nouvelle_pile()
    for x in formule :
        if type(x)==int:
            empile(x,p)
        else:
            b=depile(p)
            a=depile(p) 
            empile( applique(x, a, b), p)
    return depile(p)
formule=[3, 4, '+', 6, '++']
print(évaluation(formule))