from notas import ingresar_notas
def opcion_1():
    print("=== Ingreso de notas ===")
    lista_notas = ingresar_notas()
    print("Ingreso de notas de la lista de notas:")
    input(lista_notas)

def opcion_2():
    print("Elegiste la opción 2")

def opcion_3():
    print("Elegiste la opción 3")

def opcion_4():
    print("Elegiste la opción 4")


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            opcion_4()
        elif opcion == "0":
            print("Saliendo del sistema")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

main()