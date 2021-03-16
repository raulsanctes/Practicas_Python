print("Ingrese su contraseña")
password = input()
enlistado = list(password)
longitud = len(enlistado)


def valida_long():
    if longitud > 8:
        return (True, "Long", longitud)

def valida_noalpha():
    validador = True
    contador = 0
    for i in enlistado:
        if not i.isalnum():
            validador = True
            while validador == True and contador < longitud :
                contador += 1
                return (True, "No alpha")


def valida_minus():
    if any(chr.islower() for chr in password):
        return (True, "Minusculas")


def valida_mayus():
    if any(chr.isupper() for chr in password):
        return (True, "Mayusculas")


def valida_numero():
    if any(chr.isdigit() for chr in password):
        return (True, "Numero")


def principal():
    if (valida_long()):
        print("VERDADERO")
    else:
        print("FALSO")
    if (valida_noalpha()):
        print("VERDADERO")
    if (valida_numero()):
        print("VERDADERO")
    if (valida_mayus()):
        print("VERDADERO")
    if (valida_minus()):
        print("VERDADERO")


print(principal())