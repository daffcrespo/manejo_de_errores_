#Ejemplo de manejo de errores
#Dafne Crespo

while(True):
    try:
        mes = int(input("Digite su mes de nacimiento (1-12): "))
        if mes > 12 or mes <= 0:
            raise ValueError("Ese mes de nacimiento no es válido, debe de ser del 1 al 12")
        else: 
            print("Su mes de nacimiento es válido")
    except Exception as e:
        print("Exception : "+ repr(e)) 
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
        cerrar = input("\n¿Estás seguro que deseas cerrar el programa? (S/N) ")
        if cerrar.upper() == "S":
            print("Aplicación cerrada por usuario") 
            break
