from alumno import ingresar_estudiante, mostrar_estudiantes

def main():
    lista_estudiantes = []
    while True:
        est = ingresar_estudiante() 
        lista_estudiantes.append(est)

        continuar = input("¿Desea ingresar otro estudiante? (s/n): ")
        if continuar.lower() != "s":
            break

    mostrar_estudiantes(lista_estudiantes)

if __name__ == "__main__":
    main()
