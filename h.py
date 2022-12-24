b=[1,2,3,4,5,6,7,8,9]
d=0
f=len(b)
while d<f:
    k=min(b[d:f])
    b=[k]+b
    e=min(b[k:])
    b.insert(2,e)
    d+=1
print(b)