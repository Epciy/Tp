#1.2
class Entier:
    def __init__(self,num,res,ans) -> None:
        self.num=num
        self.res=res
        self.ans=ans
    def addition(self):
        self.res+=self.num
        return self.res
    def multiplication(self):
        self.ans*=self.num
        return self.ans




entier =Entier(8,0,2)
print(entier.addition())
print(entier.multiplication())
#3.
class Entier_:
    def __init__(self,arr=[]):
        self.arr=arr
    
entier_=Entier_([1,2,3,4])
#4.on peut utiliser "inheritance" pour hériter les methodes de premier  type abstrait et l'utiliser dans le deuxieme  type abstrait.