#1.chiffrement_lettre (l,d) renvoie la correspondance de la lettre l dans le dictionnaire d .
d={" ":" ","a":"e","b": "a","c": "i","d": "t", "e":"s","f": "n","g": "l","h": "u", "i":"r","j": "o","k": "d","l": "m", "m":"c","n": "p","o": "v", "p":"q","q": "h","r": "f","s": "b","t": "g","u":"j","v": "x","w": "y","x": "w","y": "z","z": "k"}
def chiffrement_lettre (l,d):
    if l in d :
        return d[l]
    
    return l 
l=str(input("donner une lettre alphabetique quelconque: "))
print(" la lettre ",l , "correspond a : ", chiffrement_lettre(l,d))
#2.
def chiffrement_phrase (p,d):
    dictionnaire={" ":" "}
    for char in p :
        dictionnaire[char]=d[char]
    return dictionnaire
p=str(input("donner une phrase quelconque :"))
print("nouveau dictionnaire :",chiffrement_phrase(p,d))

#3.inverse_dico (d) renvoie un nouveau dictionnaire qui inverse les clefs et les valeurs du dictionnaire d. Tester en déchiffrant la phrase précédemment codée.

def inverse_dico (d):
    dict_inverse={" ":" "}
    for char in d:
        dict_inverse[d[char]]=char
    return dict_inverse
new_dict=inverse_dico(d)
print("dictionnaire qui inverse les clefs et les valeurs du dictionnaire d :",new_dict)
print("nouveau dictionnaire en utilisant le dictionnaire inversé :",chiffrement_phrase(p,new_dict))



#4.dico_rot_13 () construit un dictionnaire correspondant au chiffrement en ROT13.
alphabit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
   
def dico_rot_13 (alphabit):
    dictionnaire={" ":" "}
    for  i in alphabit:
        dictionnaire[i]=alphabit[alphabit.index(i) + 13]      
    return dictionnaire

phrase=str(input("donner une phrase quelconque :"))

d_rot13=dico_rot_13 (alphabit)

def rot13(phrase):
    _rot13=" "
    for char in phrase:
        _rot13+=d_rot13[str(char)]
    return _rot13
print("le chiffrement de phrase: ",rot13(phrase))

#5.compte_lettres (p) construit un dictionnaire faisant correspondre chaque lettre apparaissant dans la phrase p à son nombre d'occurrences dans cette même phrase.
f = open('mystere.txt', 'r')
content = f.read()
print(set(content))

def compte_lettres (p):
    dictionary={}
    words=set(content)
    for chr in words:
        if chr.isalpha():
            dictionary[chr]=content.count(chr)
    return dictionary
print(" dictionnaire dedier pour  le calcule de nombre d'occurrance d'une lettre dans la phrase : ",compte_lettres(content))


#6.est un tri à bulles modifié pour renvoyer les clefs d'un dictionnaire d, ordonnées par valeurs décroissantes.
compte_lettre_dict=compte_lettres(content)
print('compte lettre : ',compte_lettre_dict)
mylist=list(compte_lettre_dict.items())
#print(mylist)
def tri_bulles_dico (d):
    new_dict={}
    for passesLeft in range(len(d)-1, 0, -1):
        for i in range(passesLeft):
            if d[i][1] < d[i + 1][1]:
                    d[i], d[i + 1]= d[i + 1], d[i]
    for x,y in d :
        new_dict[x]=y

    return new_dict
print("un dictionnaire d, ordonnées par valeurs décroissantes : ",tri_bulles_dico(mylist))

#7.arrays2dict (ks,vs) renvoie un dictionnaire dont les clefs correspondent au tableau ks et qui associe pour chacune de ces clefs la valeur se trouvant à la même position dans le tableau vs.
dict_tri_bull=tri_bulles_dico(mylist)
tableau_vs=[i for i in dict_tri_bull.keys()]

alpha_list=list('abcdefghijklmnopqrstuvwxyz')[::-1]

def arrays2dict (ks,vs):
    arraydict={" ":" "}
    for i in range(len(vs)):
        arraydict[vs[i]]=ks[i]
    
    return arraydict
print("un dictionnaire dont les clefs correspondent au tableau alpha_list  et qui associe pour chacune de ces clefs la valeur se trouvant à la même position dans le tableau_vs: ",arrays2dict (alpha_list,tableau_vs))

#8.decrypte (pc,ll) doit décrypter la phrase pc à l'aide des lettres de l'alphabet rangées par ordre de fréquence décroissante dans la langue utilisée et disponible dans le tableau ll
def decrypte (pc,ll):
   
    f = open('decrpte.txt','a')
    for chr in pc  :
        if chr in ll:
            f.write(ll[chr])
            
        else:
            f.write(str(chr)) 
    f.write("\n") 
    f.close()     
arraysdict=arrays2dict(alpha_list,tableau_vs)
#decrypte (content,arraysdict)