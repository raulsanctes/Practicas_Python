print("Ingrese su usuario")
nombre = input()
usuarioValido = nombre.isalnum()


def valida_len():
    if len(nombre) < 6:
        print("El nombre de usuario debe contener al menos 6 caracteres")
        return False
    elif len(nombre) > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
        return False
    else:
        return True


def valida_alfa():
    if usuarioValido is True:
        return True
    elif usuarioValido is False:
        print("El nombre de usuario solo puede contener solo letras y números")
    else:
        return False


def main():
    if valida_len() is True:
        if valida_alfa() is True:
            print("Registrado con éxito")
            return True
    else:
        return False


print(main())