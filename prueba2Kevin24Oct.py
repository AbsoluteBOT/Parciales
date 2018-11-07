# Crea una Tupla con los meses del anno, pide numeros al usuario, si el 
# numero esta entre 1 y la longitud maxima de la tupla, muestra el cont-
# enido de esa posicion sino muestra un mensaje de error. 

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
salir = False
while(not salir):
     
    numero = int(input("Dame un numero: "))
 
    if(numero==0):
        salir= True
    else:
        if(numero ==1 ):
            print("Enero")
        elif (numero ==2) :
			print ("Febrero")
        elif (numero ==3) :
			print ("Marzo")
        elif (numero ==4):
			print ("Abril")
        elif (numero ==5):
			print ("Mayo")
        elif (numero ==6):
			print ("Junio") 
        elif (numero ==7) :
			print ("Julio")
        elif (numero ==8):
			print ("Agosto")
        elif (numero ==9) : 
			print ("Septiembre") 
        elif (numero ==10) :
			print ("Octubre") 
        elif (numero ==11) : 
			print ("Noviembre") 
        elif (numero ==12) : 
			print ("Diciembre")
			
        else:
            print("ERORR!, Inserta un numero entre 1 y 12") 

#22
            
 # ~ """

 # ~ Crea un diccionario donde la clave sea el nombre del usuario y el
 # ~ valor sea el telefono. Tendras que ir pidiendo contactos hasta el
 # ~ usuario diga que no quiere inertar mas. No se podran meter nombres repetidos.
 
# ~ """

agenda = {"Kevin" : 0416,"raul":0212}
 
salir = False
 
while (not salir):
 
    
    nombre= raw_input ("Introduce un nombre : ")
    telefono=int(input("Introduce un telefono: "))
 
    
    if(nombre not in agenda):
       
        agenda[nombre] = telefono
        print("Contacto agregado")
    else:
        print("El contacto ya esta agregado")
         
    
    respuesta = raw_input (" Quieres salir? (S/N): ")
 
    if(respuesta == "S"):
        salir = True
    elif (respuesta == "s") : 
		salir = True
    elif (respuesta == "N") : 
		salir = False
    elif (respuesta == "n"): 
		salir = False

print(agenda)

 # ~ """

 # ~ Pide un numero por teclado y guarda en una lista su tabla de 
 # ~ multiplicar hasta el 10. Por ejemplo, si pide el 5 la list tendra
 # ~ [5,10,15,20,25,30,35,40,45,50]
 
# ~ """


liss=[ ]

numero = raw_input ("Introduce numero") 






# Kevin Martinez 
# Cedula : 23.607.297 
# UNEFA Lenguaje de Programacion 2 
# 24 de Octubre de 2018


