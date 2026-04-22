# ============================================
# Módulo: Notas.py
# Autor: [Pablo Diaz]
# Descripción: Funciones para gestionar notas de estudiantes
# ============================================

# ============================================
# Gestion de notas de 5 alumnos
# ============================================

def ingresar_notas_alumno(nombre, num_notas=3):
    """
    Para un alumno dado, ingresa sus 'num_notas' notas.
    Retorna una lista con esas notas.
    """
    notas = []
    print(f"\n--- Ingresando notas de {nombre} ---")
    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Nota {i+1}: "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 20.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    return notas

def calcular_promedio(notas):
    """Recibe lista de notas y retorna el promedio."""
    if not notas:
        return 0
    return sum(notas) / len(notas)

def condicion_alumno(promedio, nota_aprobatoria=11):
    """Retorna 'APROBADO' o 'DESAPROBADO' según el promedio."""
    return "APROBADO" if promedio >= nota_aprobatoria else "DESAPROBADO"

def mostrar_reporte_alumno(nombre, notas):
    """Muestra el reporte individual de un alumno."""
    promedio = calcular_promedio(notas)
    cond = condicion_alumno(promedio)
    print(f"\n--- Reporte de {nombre} ---")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Condición: {cond}")

def procesar_grupo(cantidad_alumnos=5, num_notas_por_alumno=3):
    """
    Procesa un grupo completo de alumnos.
    Retorna una lista de diccionarios con los datos de cada alumno.
    """
    grupo = []
    for i in range(cantidad_alumnos):
        nombre = input(f"\nNombre del alumno {i+1}: ").strip()
        if nombre == "":
            nombre = f"Alumno_{i+1}"
        notas = ingresar_notas_alumno(nombre, num_notas_por_alumno)
        grupo.append({
            "nombre": nombre,
            "notas": notas,
            "promedio": calcular_promedio(notas),
            "condicion": condicion_alumno(calcular_promedio(notas))
        })
    return grupo

def reporte_general(grupo):
    """Muestra un reporte general de todo el grupo."""
    print("\n" + "="*40)
    print("REPORTE GENERAL DEL GRUPO")
    print("="*40)
    for alumno in grupo:
        print(f"{alumno['nombre']}: {alumno['notas']} -> Prom: {alumno['promedio']:.2f} ({alumno['condicion']})")
    
    promedios = [a['promedio'] for a in grupo]
    promedio_grupo = sum(promedios) / len(promedios)
    aprobados = sum(1 for a in grupo if a['condicion'] == "APROBADO")
    print(f"\nPromedio del grupo: {promedio_grupo:.2f}")
    print(f"Aprobados: {aprobados} / {len(grupo)}")

# ============================================
# Ejecución principal (para 5 alumnos)
# ============================================
if __name__ == "__main__":
    print("=== SISTEMA DE NOTAS PARA 5 ALUMNOS ===")
    print("Cada alumno tendrá 3 notas.")
    grupo = procesar_grupo(cantidad_alumnos=5, num_notas_por_alumno=3)
    reporte_general(grupo)