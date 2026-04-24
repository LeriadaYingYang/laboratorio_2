# =======================================
# Módulo: validacion.py
# Autor: [Fabrizio]
# Descripción: Función para validar promedios de estudiantes
# =======================================

# =======================================
# FUNCIONES DE PROMEDIO
# =======================================

def calcular_promedio(notas):

    if len(notas) == 0:
        return 0

    return sum(notas) / len(notas)


def obtener_estado(promedio):

    if promedio >= 11:
        return "Aprobado"
    else:
        return "Desaprobado"


# =======================================
# Validación.py - Devuelve una letra y un estado
# =======================================


def validar_promedio(promedio):

    # Si no existe promedio
    if promedio is None:
        return None, "Sin datos"

    # Clasificación por rangos
    if 18 <= promedio <= 20:
        return "AD", "Sobresaliente"

    elif 15 <= promedio <= 17:
        return "A", "Aprobado"

    elif 11 <= promedio <= 14:
        return "B", "Regular"

    elif 0 <= promedio <= 10:
        return "C", "Desaprobado"

    else:
        return None, "Promedio inválido"