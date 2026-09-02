#Ejercicio 1

materias = ['Filosofia', 'Ingles', 'Matematicas', 'Historia', 'Fisica']

materias.append('Quimica')

del materias[0]

print(materias[::-1])

#Ejercicio 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [num for num in numeros if num % 2 == 0]

cuadrados = [num * num for num in numeros]

print(pares)
print(cuadrados)

#Ejercicio 3

plan = {
    "mes_1": "Python + matemáticas",
    "mes_2": "Machine learning clásico",
    "mes_3": "Deep learning + PyTorch",
    "mes_4": "NLP + Arquitectura de transformers",
    "mes_5": "LLMs, Fine tuning y RAG",
    "mes_6": "Portafolio y despliegue",
    "mes_7": "Entrevista y postulacion diversificada"
}

for mes, tema in plan.items():
    print(f'En el {mes}, se estudia {tema}')

print(plan.get("mes_4"))

#Ejercicio 4

python_basico = ["variables", "loops", "funciones", "listas"]
python_intermedio = ["funciones", "clases", "decoradores", "listas"]


interseccion = set(python_basico).intersection(set(python_intermedio)) #Puedes usar '&' para esto
intermedio = set(python_intermedio).difference(set(python_basico)) #Puedes usar '-' para esto

print(interseccion)
print(intermedio)

#Ejercicios 5

dias_estudiados = [
    {"dia": 1, "horas": 6, "tema": "listas y tuplas"},
    {"dia": 2, "horas": 7, "tema": "funciones"},
]

def resumen_semana(dias_estudiados):
    total = sum(d["horas"] for d in dias_estudiados)
    dia_max = max(dias_estudiados, key=lambda d: d["horas"]) if dias_estudiados else None
    promedio = total / len(dias_estudiados) if dias_estudiados else 0
    return {
        'promedio de horas/dia': promedio,
        'total de horas': total,
        'tema': dia_max["tema"]
    }

print(resumen_semana(dias_estudiados))

