import re 
class IPv4:
    def __init__(self, ip):
        self.ip = ip

    def validarLongitud(self, cadena):
        if len(cadena) > 3:
            return False
        else:
            numero = int(cadena)
            if (len(str(numero)) != len(cadena)):
                return False
            return (numero >= 0) & (numero <= 255)
    
    def validarCadena(self):
        valido = True
        arregloNumeros = self.ip.split(".")
        if(len(arregloNumeros) == 4):
            for cadena in arregloNumeros:
                if(re.match(r'^([\s\d]+)$', cadena)):
                    if(valido):
                        valido = self.validarLongitud(cadena)
                else:
                    valido = False    
        else:
            valido = False

        if (valido): 
            return "Valido"
        else:
            return "Invalido"
        
