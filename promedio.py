# --- FUNCIÓN CON PARÁMETROS Y RETORNO ---
def calcular_promedio(nota1, nota2, nota3):
    """
    Esta función recibe 3 notas como parámetros,
    calcula el promedio y lo devuelve con return.
    """
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio  # Aquí se usa el comando obligatorio 'return'

# --- FLUJO PRINCIPAL DEL PROGRAMA ---
print("=========================================")
print("   PROGRAMA PARA CALCULAR EL PROMEDIO    ")
print("=========================================")

# Solicitamos los datos al usuario
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# LLAMADA A LA FUNCIÓN: Pasamos las notas y guardamos lo que devuelve en 'resultado'
resultado = calcular_promedio(nota1, nota2, nota3)

# MOSTRAR RESULTADO EN PANTALLA
print("-----------------------------------------")
print(f"El promedio de las tres notas es: {resultado:.2f}")
print("-----------------------------------------")
