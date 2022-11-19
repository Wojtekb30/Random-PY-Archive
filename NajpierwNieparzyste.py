import random
x=0
y=0
ran = 0
N=10
A = []
B = []
 
def losuj(x=0, ran=0):
    while x<N:
        ran = random.randint(1,100)
        A.append(ran)
        
        x=x+1
    x=0
    
def sortuj(x=0, y=0, B=[]):
    while x<N:
        B.append(0)
        x=x+1
    x=0
    while x<N:
    
        if A[x]%2==1:
            B[y]=A[x]
            A[x]=0
            y=y+1
        x=x+1
    
    x=0
    while x<N:
        if A[x]!=0:
            B[y]=A[x]
            y=y+1
        x=x+1
    
    x=0
    while x<N:
        A[x]=B[x]
        x=x+1
    
    
losuj()

while x<N:
    print(A[x])
    x=x+1

x=0

sortuj()

print("Posortowane: ")

while x<N:
    print(A[x])
    x=x+1
