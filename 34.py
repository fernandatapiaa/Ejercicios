print ("1 square")
print ("2 triangle")
a=int(input("ingresa un numero del 1 al 2"))
if a==1:
    b=int(input("ingresa el lado"))
    print(b*b)
elif a==2:
    c= int(input("ingresa la base"))
    e=int(input("ingresa la altura"))
    print(c*e/2)
else:
    print ("suitable error message")