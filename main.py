from notas import ingresar_notas
from validacion import validar_promedio
lista_notas_global = []
def opcion_1():
    print("=== Ingreso de alumnos===")

def opcion_2():
    global lista_notas_global
    print("=== Ingreso de notas ===")
    lista_notas_global = ingresar_notas()
    print("Notas registradas:", lista_notas_global)
    input()

def opcion_3():
    global lista_notas_global
    print("=== Validación ===")

    if not lista_notas_global:
        print("Primero debes ingresar notas.")
        return
    promedio = sum(lista_notas_global) / len(lista_notas_global)
    letra, estado = validar_promedio(promedio)
    print(f"Promedio: {promedio:.2f}")
    print(f"Resultado: {letra} {estado}")
    input()

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