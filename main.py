from notas import ingresar_notas
from promedios import calcular_promedio, obtener_estado


def opcion_1():
    print("=== Ingreso de notas ===")
    
    lista_notas = ingresar_notas()

    print("\nNotas ingresadas:")
    for i, nota in enumerate(lista_notas, start=1):
        print(f"Nota {i}: {nota}")

    promedio = calcular_promedio(lista_notas)
    estado = obtener_estado(promedio)

    print(f"\nPromedio: {promedio:.2f}")
    print(f"Estado: {estado}")


def opcion_2():
    print("Opción 2 aún no implementada")


def opcion_3():
    print("Opción 3 aún no implementada")


def opcion_4():
    print("Opción 4 aún no implementada")


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Ingresar notas y calcular promedio")
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


if __name__ == "__main__":
    main()
