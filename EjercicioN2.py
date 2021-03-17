class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def valida_pass(password):

    enlista = list(password)
    if len(enlista) > 8 :
        print(bcolors.OKGREEN +"Longitud OK")
        if any(chr.isdigit() for chr in password):
            print(bcolors.OKGREEN +"Digitos OK")
            if any(chr.isalpha() for chr in password):
                print(bcolors.OKGREEN +"Alfanumerico OK")
                if any(chr.isalnum() != True for chr in password):
                    print(bcolors.OKGREEN +"Caracter Especial OK")
                    if any(chr.isspace() != True for chr in password):
                        print(bcolors.OKGREEN +"No espacios OK")
                        if any(chr.islower() for chr in password):
                            print(bcolors.OKGREEN +"Minuscula OK")
                            if any(chr.isupper() for chr in password):
                                print(bcolors.OKGREEN +"Mayusculas OK")
                        print(bcolors.OKCYAN + "CONTRASEÑA VALIDA" + bcolors.ENDC)
                        return True
    print(bcolors.WARNING + "Contraseña no válida" + bcolors.ENDC)
    return False

clave = input(bcolors.HEADER + "Ingrese una contraseña\n" + bcolors.ENDC)

print(valida_pass(clave))