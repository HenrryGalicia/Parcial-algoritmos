mail = input("Ingrese un mail:") #Se quito un signo = 
cantidad = 0  #le asigne 0 a la variable 
x = 0 #separe y quite un signo =  
while x < len(mail): #se separo la x y < y sustitui leng por len 
    if mail[x] == "@": #correcto
        cantidad += 1  # se le agrego un = al +1 y se quito cantidad
    x += 1  # se cambio x=x++1 por x += 1
if cantidad == 1: # correcto
    print("Contiene solo un caracter @ el mail ingresado")  
else:
    print("Incorrecto")  #Se le agrego una comilla al inicio de incorrecto
