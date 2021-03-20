import EjercicioN1
import EjercicioN2

correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if EjercicioN1.nickname(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if EjercicioN2.clave(contrasenia)==True:
        print("Contraseña creada exitosamente")
        correcto=False