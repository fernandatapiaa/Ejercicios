name= input ('Ingresa tu nombre ')
leng= len(name)
if leng<5:
    n= input ('Ingresa tu apellido ')
    word= name+n 
    print (word.upper())
else:
    print(name.lower())
