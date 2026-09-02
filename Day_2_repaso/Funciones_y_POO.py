# Ejercicio N.1

def calcular_horas_totales(*num):
    return sum(num)

print(calcular_horas_totales(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def describir_dia(**kwards):
    for key, value in kwards.items():
        print(f'{key}: {value}')

describir_dia(dia=2, horas=6, tema="POO y funciones")

# Ejercicios N.2

numeros = [1, 2, 3, 4, 5]

def al_cuadrado(x):
    return x ** 2

def aplicar_operacion(funcion, lista):
    return [funcion(x) for x in lista]



print(aplicar_operacion(al_cuadrado, numeros))
print(aplicar_operacion(lambda x: x ** 2, numeros))

# Ejercicio N.3

class DiaDeEstudio:
    def __init__(self, dia, horas, temas):
        self.dia = dia
        self.horas = horas
        self.temas = temas

    def resumen(self):
        return f'Dia {self.dia}: {self.horas} horas de estudio sobre {self.temas}'
        

datos = DiaDeEstudio(2, 6, "POO y funciones")
print(datos.resumen())

datos2 = DiaDeEstudio(3, 3, "Listas y diccionarios")
datos2.resumen()

# Ejercicio N.4

class DiaConProyecto(DiaDeEstudio):
    def __init__(self, dia, horas, tema, proyecto):
        super().__init__(dia, horas, tema)
        self.proyecto = proyecto

    def resumen(self):
        return f'Dia {self.dia}: {self.horas} horas de estudio sobre {self.temas} y se trabajó en el proyecto: {self.proyecto}'


dato3 = DiaConProyecto(4, 7, "Funciones de orden superior", "Proyecto de funciones")
dato3.resumen()

# Ejercicio N.5

class SemanaDeEstudio:
    def __init__(self, datos):
        self.datos = datos

    def total_horas(self):
        return sum(d.horas for d in self.datos)
        
    def dia_mas_largo(self):
        return max(self.datos, key=lambda d: d.horas)
        

                



dat = SemanaDeEstudio([datos, datos2])

print(dat.total_horas())

dia = dat.dia_mas_largo()

print(dia.dia)

        
            
    
        
        





