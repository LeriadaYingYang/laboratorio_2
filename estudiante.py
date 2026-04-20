def crear_estudiante(codigo, nombre, apellido, celular, dni, edad):
    estudiante_generico = {"Codigo":codigo, 
                           "Nombre":nombre, 
                           "Apellido":apellido, 
                           "Celular":celular, 
                           "Dni": dni, 
                           "Edad": edad}
    return estudiante_generico

def mostrar_estudiantes(lista_estudiantes):
    for i in lista_estudiantes: 
        print(f"Estudiante: {i['Nombre']} {i['Apellido']} Codigo: {i['Codigo']}")