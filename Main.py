from TDA.MaxNumber import MaxNumber
from TDA.IPv4 import IPv4
from TDA.Addition import Addition
from TDA.Candys import Candys

while(True):
    print("---------------------------------------")
    opcion = int(input("Introduce una opción: \n\t1) Número más grande dependiendo el número de digitos\n\t2) Validar IPv4\n\t3) Suma de un número de 2 digitos\n\t4) Niños y Dulces \n\t5) Salir\n\t => "))
    print("---------------------------------------\n\n")
    if (opcion == 1):
        ##Numero Max
        n = int(input("Introduce Un Número: "))
        numeroMax = MaxNumber(n)
        print(str(int(numeroMax.getResult()))+"\n\n")
    elif (opcion == 2):
        ## IPv4
        ip = input("Introduce Tu IPv4: ")
        validadorIPv4 = IPv4(ip)
        print(str(validadorIPv4.validarCadena())+"\n\n")
    elif (opcion == 3):
        ##Suma
        num = int(input("Introduce Un Número (Dos digitos): "))
        if(len(str(num)) == 2):
            suma = Addition(num)
            print(str(suma.getResult())+"\n\n")
        else:
            print("Error. Número no valido")
    elif (opcion == 4):
        ##Dulces
        ninos = int(input("Introduce el número de niños: "))
        dulces = int(input("Introduce la cantidad de dulces: "))
        totalDulces = Candys(ninos, dulces)
        print(str(totalDulces.obtenerResultado())+"\n\n")
    elif (opcion == 5):
        print("¡Adios!\n\n")
        break
    else:
        print("Opción no valida")

    
