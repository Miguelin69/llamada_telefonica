print("...................................................................")
print("......................llamada telefonica...........................")
print("...................................................................")


# imput 

n=int(input("digite el tiempo de su llamada: "))
J= 300



# output


if n<3 :

    rta= ("el costo de su llamada es: "  + str (J))

   
else: 
     
     P= (n-3)
     A= (P*50)
     Y= (J+A)
     rta = "el costo de su llamada es: " + str(Y)

print( str (rta))