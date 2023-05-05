# Función para calcular el área de un triángulo
def calcular_area(b, a):
    ar = (b * a) / 2
    return area

# Pedir al usuario valores
b = float(input("Ingresa la base del triángulo: "))
a = float(input("Ingresa la altura del triángulo: "))

# Calcular el área 
ar = calcular_area(b, a)

# Mostrar el resultado
print("El área del triángulo es:", ar)
