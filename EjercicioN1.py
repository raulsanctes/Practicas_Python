"""Ejercicio No1
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá
cumplir con los siguientes criterios de aceptación:

--> El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12 OK
--> El nombre de usuario debe ser alfanumérico OK
--> Nombre de usuario con menos de 6 caracteres, retorna el mensaje “El nombre de
    usuario debe contener al menos 6 caracteres” OK
--> Nombre de usuario con más de 12 caracteres, retorna el mensaje “El nombre de
    usuario no puede contener más de 12 caracteres” OK
--> Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje
    “El nombre de usuario puede contener solo letras y números”
--> Nombre de usuario válido, retorna True """

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