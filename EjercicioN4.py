# De un rango de números
# extraer solo los números pares
print("Ingrese dos numeros enteros")

n1 = int(input())
n2 = int(input())
    
def calculo(n1, n2):    
    rango = list(range(n1, n2 + 1))   
    print("Los numeros pares son")
    for i in rango:
        i = i / 2
        cadena = str(i)
        if cadena.endswith(".0"):
            cadena = int(i)
            cadena = cadena * 2
            print(cadena)

    return True

print(calculo(n1, n2))
