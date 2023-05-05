def suma (a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    
    if b == 0:
        return "No se puede dividir entre cero "
    else:
        return a / b


helo = 'hola'
mau = [1,2]
dicc = {}
mau = 1 & 1 | 2


#Provamos todas las funciones y esperamos sus resutados
print(suma(2, 3)) 
print(resta(6, 4)) 
print(multiplicacion(13, 2)) 
print(division(10, 2))
print(division(8, 0))
