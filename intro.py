 nombre = input ("Escribe tu nombre")
 print (nombre)
 print (len(nombre))
 
 if len(nombre) >= 12:
    print ("Contraseña fuerte")
elif len (nombre)<12 and len (nombre)>6:
    print ('Contrasena media')
else:
    print ("Contrasena debil")
