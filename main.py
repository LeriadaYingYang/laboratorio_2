import estudiante as est

def agregar_estudiante(lista, codigo, nombre, apellido, celular, dni, edad):
    lista.append(est.crear_estudiante(codigo, nombre, apellido, celular, dni, edad)) 

def mostrar(lista):
    est.mostrar_estudiantes(lista)

def opcion_3():
    print("Elegiste la opción 3")

def opcion_4():
    print("Elegiste la opción 4")


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar Estudiante")
    print("2. Mostrar todod los estudiantes")
    print("3. Opción 3")
    print("4. Opción 4")
    print("0. Salir")

def main(lista):
    while True:
        mostrar_menu()

        opcion = int(input("Selecciona una opción: "))

        match opcion: 
            case 1: 
                codigo = input("Indique el codigo del estudiante nuevo: ")
                nombre = input("Indique el nombre del estudiante nuevo: ")
                apellido = input("Indique el apellido del estudiante nuevo: ")
                celular = input("Indique el celular del estudiante nuevo: ")
                dni = input("Indique el dni del estudiante nuevo: ")
                edad = input("Indique la edad del estudiante nuevo: ")
                agregar_estudiante(lista, codigo, nombre, apellido, celular, dni, edad)
            case 2: 
                mostrar(lista)
            case _: 
                print("Selecciona una opcion valida")

lista_estudiantes = []

lista_estudiantes.append(est.crear_estudiante("0123", "Lucas", "Montenegro", "987654321", "12345678", 19))
lista_estudiantes.append(est.crear_estudiante("0124", "Maria", "Diaz", "987654352", "12348278", 17))
lista_estudiantes.append(est.crear_estudiante("0125", "Edith", "Wingo", "936294352", "12372478", 21))

main(lista_estudiantes)