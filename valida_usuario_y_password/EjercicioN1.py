def nickname(nombre_usuario):

        long=len(nombre_usuario) 
        y=nombre_usuario.isalnum()
        
        if y== False:
            print("El nombre de usuario puede contener solo letras y números")
            
        if long < 6: 
            print("El nombre de usuario debe contener al menos 6 caracteres")
            
        if long > 12: 
            print("El nombre de usuario no puede contener más de 12 caracteres")
            
        if long >5 and long <13 and y ==True:
            return True 