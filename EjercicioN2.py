print("Ingrese su contraseña")
password = input()
enlistado = list(password)
longitud = len(enlistado)


def error():
    print("LA CONTRASEÑA ELEGIDA NO ES SEGURA")
    return True


def valida_long():
    if longitud >= 8:
        return True
    else:
        print("LONGITUD NO VALIDA")
        error()


def valida_noalpha():
    if any(chr.isalnum() == True for chr in password):
        return True
    else:
        print("DEBE TENER AL MENOS UN CARACTER ALFANUMERICO")
        error()


def valida_alpha():
    if any(chr.isalnum() != True for chr in password):
        return False
    else:
        print("DEBE TENER AL MENOS UN CARACTER ESPECIAL")
        error()


def valida_minus():
    if any(chr.islower() for chr in password):
        return True
    else:
        print("DEBE TENER MINUSCULA")
        error()


def valida_mayus():
    if any(chr.isupper() for chr in password):
        return True
    else:
        print("DEBE TENER MAYUSCULA")
        error()


def valida_numero():
    if any(chr.isdigit() for chr in password):
        return True
    else:
        print("DEBE TENER UN NUMERO")
        error()


def valida_espacio():
    for i in enlistado:
        if i.isspace() != False:
            print("NO USE ESPACIOS")
            return True
            error()


def principal():
    print(valida_long(), "LONGITUD")
    print(valida_espacio(), "ESPACIO")
    print(valida_alpha(), "ALFANUMERICO OK")
    print(valida_noalpha(), "NO ALFANUMERICO")
    print(valida_mayus(), "MAYUSCULA")
    print(valida_minus(), "MINUSCULA")
    print(valida_numero(), "NUMERO")
    return "PASO"


print(principal())
