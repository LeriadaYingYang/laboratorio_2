from validacion import calcular_promedio, validar_promedio, obtener_estado

def main():

    notas = []

    print("=== REGISTRO DE NOTAS ===")

    for i in range(3):

        while True:
            try:
                nota = float(input(f"Ingrese nota {i+1} (0-20): "))

                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("Error: la nota debe estar entre 0 y 20.")

            except ValueError:
                print("Error: ingrese un número válido.")

    promedio = calcular_promedio(notas)

    letra, descripcion = validar_promedio(promedio)

    estado_general = obtener_estado(promedio)

    print("\n=== RESULTADO FINAL ===")
    print("Notas ingresadas:", notas)
    print("Promedio:", round(promedio, 2))
    print("Nivel:", letra)
    print("Descripción:", descripcion)
    print("Estado general:", estado_general)


if __name__ == "__main__":
    main()