from Library import Library, Usuario

libreria = Library(
        ["economia", "python", "java", "matematicas1", "calculo", "fisica1", "fisica2", "dinamica", "estatica"])
usuario = Usuario()

print("BIENVENIDO\n")
print("""Escoge una opcion:-\n1. Ver libros\n2. Prestar libros\n3. Devolver libros\n4. salir\n""")

while (True):
    try:
        casos = int(input("ESCOGE: "))

        if casos == 1:  
            libreria.disponibilidad()
        elif casos == 2: 
            libreria.prestar(
                input("INGRESA TU NOMBRE: "), usuario.solicitar())
        elif casos == 3:  
            libreria.devuelto(usuario.devolver())
        elif casos == 4:
            pista= []
            for i in pista:
                for key, value in i.items():
                    poseedor = key
                    book = value
                    print(f"{book} libro cogido por:  {poseedor}.")
            print("\n")
            if len(pista) == 0:
                print("LIBRO EMITIDO!. \n")
            
        elif casos == 4:
            print("GRACIAS! \n")
            exit()
        else:
            print("EROOR! \n")
    except Exception as e:    
        print(f"{e} -> INVALIDO! \n")