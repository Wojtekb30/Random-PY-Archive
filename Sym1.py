global numitr
numitr = 0
def sym (a, b):

    if a!=0:
        sym(a-1, b+1)
 #       print("a1: "+str(a))
  #      print("b1: "+str(b))
        print(a*b)
        global numitr
        numitr = numitr +1
        sym(a-1, b+1)
   #     print("a2: "+str(a))
   #     print("b2: "+str(b))
a = int(input("a "))
b = int(input("b "))
print(" ")
sym(a, b)
print(" ")
print(numitr)
