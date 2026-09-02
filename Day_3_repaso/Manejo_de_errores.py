#Ejercicio N.1

def dividir_horas(horas, dias):
    try:
        return horas / dias
    except Exception as error: #El error tambien puede capturarse especificamente usando su 'Tipo de excepcion'
        return f'A ocurrido un error, informacion del error: {error}' 

print(dividir_horas(10, 5))
print(dividir_horas(10, 0))

#Ejercicio N.2

def convertir_horas(texto):
    try:
        return float(texto)
    except ValueError:
        return 'El texto no es valido'

print(convertir_horas('6'))
print(convertir_horas('6.5'))
print(convertir_horas('seis'))

#Ejercicio N.3

class HorasInvalidasError(Exception):
    def __init__(self, horas):
        self.horas = horas
        super().__init__(f'Error, la hora {horas}, no es valida para el formato de 24H')

    def __str__(self):
        return f'El valor que introdujo: {self.horas}, no es correspondiente para el formato de 24H'


def validar_horas(horas):
    if horas < 0 or horas > 24:
        raise HorasInvalidasError(horas)
    return f'Las {horas} horas es un numero valido'

try:
    print(validar_horas(2))
    print(validar_horas(25))
except HorasInvalidasError as e:
    print(f"Ocurrió un error: {e}")


#Ejercicio N.4

#>Simulacion de guardado

def guardar_progreso(progreso):
    try: 
        if 0 <= progreso <= 100:
            print(f'Tu progreso {progreso}, es valido')
        else:
            raise ValueError()
    except ValueError: #Puedes capturar raise ValueError dentro del bloque de codigo
        print('El progreso no es valido')
    except TypeError:
        print('Escribe un numero')

    finally:
        print('Guardando...')
        print('-Progreso guardado-')


guardar_progreso(102)



try:
    raise ValueError('Note: El progreso debe estar en el rango de 1-100')
except ValueError as e:
    print(e)

guardar_progreso("hola")






    

    




        

    



