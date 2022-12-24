import copy
#from pygnuplot import gnuplot
#1. 
tableau_t=[5,12,9,20,58,10,14]
def copie(t):
    newlist=t.copy()
    return newlist
copie_t=copie(tableau_t)

#2.
def inverse(t):
    return t[::-1]
#3.

def tableau_premiers_entiers (n):
    tab=[i for i in range(n+1)]
    return tab

n=int(input("donner un nombre entier quelconque : "))
tab_n=tableau_premiers_entiers (n)
import random
tab_premier_ent=tableau_premiers_entiers(n)
def tableau_premiers_entiers_melanges (n):
    random.shuffle(n) 
    return n
    
def tableau_premiers_entiers_inverses (n):
    tab_inv=inverse(n)
    return tab_inv

#4.
def ligne_dans_fichier (f,n,t):
    file = open(f,'a')
    file.write(str(n))
    file.write("\t")
    file.write(str(t))
    file.write("\n")        
    file.close() 

# ligne_dans_fichier("fichier.txt",5,10)

#5.
import time
def temps_tri_bulles(t) :
    cop_tab=copie(t)
    for i in range(len(cop_tab)):
        for j in range(0, len(cop_tab) - i - 1):
            if cop_tab[j] > cop_tab[j + 1]:
                cop_tab[j],cop_tab[j+1]=cop_tab[j+1],cop_tab[j]
    tmp=time.process_time()
    #print(cop_tab)
    return tmp
print("temp necessaire pour tri bulles:",temps_tri_bulles(tableau_t) ,"sec.")

#6.




def stats_melange (nmin,nmax,pas,fois):
    step=0
    res=[]
    n=nmin
    while nmin<=n<=nmax and step<=fois:
        arr=[i for i in range(n)]
        random.shuffle(arr)
        res.append(arr)
        n+=pas
        step+=1
    for tab in res :
        tmp=temps_tri_bulles(tab)
        ligne_dans_fichier("tmp_tableau_melangé.dat",len(tab),tmp)
    return 
 
#stats_melange(100,1000,100,5)
#7.


def stats_ordonne (nmin,nmax,pas,fois):
    step=0
    tab=[]
    n=nmin
    while nmin<=n<=nmax and step<=fois:
        arr=[i for i in range(n)]
        tab.append(arr)
        n+=pas
        step+=1
    #print(tab)
    for t in tab :
        tmp=temps_tri_bulles(t)
        ligne_dans_fichier ("tmp_tableau_ordonne.dat",len(t),tmp)
    return tab
#stats_ordonne(100,1000,100,5)
#8.

def stats_inverse (nmin,nmax,pas,fois):
    step=0
    tab_ord=[]
    n=nmin
    while nmin<=n<=nmax and step<=fois:
        arr=[i for i in range(n,-1,-1)]
        tab_ord.append(arr)
        n+=pas
        step+=1
    #print(tab_ord)
    for tab in tab_ord :
        tmp=temps_tri_bulles(tab)
        ligne_dans_fichier ("tmp_tableau_inverse.dat",len(tab),tmp)
    return 
 
#stats_inverse(100,1000,100,5)

#9.
def evolution_tmp(nmin,nmax,pas,fois):
    stats_melange (nmin,nmax,pas,fois)
    stats_ordonne (nmin,nmax,pas,fois)
    stats_inverse (nmin,nmax,pas,fois)
    return 

# plot :plot "tmp_tableau_melangé.dat" title "tableaux mélangés" lt 11 lc 3 w lp  ,"tmp_tableau_ordonne.dat" title "tableaux ordonnées" lt 12 lc 1 w lp  ,"tmp_tableau_inverse.dat" title "tableau inversés" lt 22 lc 5 w lp  
#evolution_tmp(100,1000,100,5)




#10.11.
# on va importer tous les fonctions des differents tri dans le fichier tri.py
from tri import tri_extraction,tri_insertion,time_tri_rapide,tri_rapide
def different_tri(nmin,nmax,pas,fois):
    step=0
    res=[]
    n=nmin
    while nmin<=n<=nmax and step<=fois:
        arr=[i for i in range(n)]
        random.shuffle(arr)
        res.append(arr)
        n+=pas
        step+=1
    for tab in res :
        tmp0=temps_tri_bulles(tab)
        ligne_dans_fichier("tri_bulle.dat",len(tab),tmp0)
        tmp1=tri_insertion(tab)
        ligne_dans_fichier("tri_insertion.dat",len(tab),tmp1)
        tmp2=tri_extraction(tab)
        ligne_dans_fichier("tri_extraction.dat",len(tab),tmp2)
        tmp3=time_tri_rapide(tri_rapide(tab))
        ligne_dans_fichier("tri_rapide.dat",len(tab),tmp3)
        
    return
different_tri(100,1000,100,5)

#le plot commande: plot "tri_bulle.dat" title "tri bulles" lt 11 lc 3 w lp  ,"tri_extraction.dat" title "tri extraction" lt 12 lc 9 w lp  ,"tri_insertion.dat" title "tri insertion" lt 22 lc 7 w lp ,"tri_rapide.dat" title "tri rapide" lt 18 lc 2 w lp

 

    