def contar_letra_en_string(cadena, letra):
    """
    Esta función cuenta cuántas veces aparece la letra en la cadena (mayúsculas o minúsculas).
    """
    cadena = cadena.lower()
    letra = letra.lower()
    
    contador = cadena.count(letra)
    return contador

def calcular_suma_promedio(valores):
    """
    Esta función calcula la suma y el promedio de un conjunto de valores.
    """
    valores = [float(valor) for valor in valores]
    
    suma = sum(valores)
    promedio = suma / len(valores)
    
    return suma, promedio

if __name__ == "__main__":
    cadena_opcion = "Algoritmos"
    letra_opcion = "a"
    resultado = contar_letra_en_string(cadena_opcion, letra_opcion)
    print(f"La letra '{letra_opcion}' aparece {resultado} veces en la cadena '{cadena_opcion}'.")
    
    valores_opcion = input("Ingrese los valores separados por comas: ").split(',')
    suma_opcion, promedio_opcion = calcular_suma_promedio(valores_opcion)
    print(f"La suma de los valores es: {suma_opcion}")
    print(f"El promedio de los valores es: {promedio_opcion}")
