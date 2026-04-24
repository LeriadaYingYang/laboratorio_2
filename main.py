from alumno import ingresar_estudiante, mostrar_estudiantes
print("PROBANDO EJECUCION")

def main():
    lista_estudiantes = []
    est = ingresar_estudiante()
    lista_estudiantes.append(est)
    mostrar_estudiantes(lista_estudiantes)
if __name__ == "__main__":
    main()