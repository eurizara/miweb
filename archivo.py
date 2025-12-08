##print("Hola mundo")
Nombre = input("Ingrese su nombre completo: ")
def saludar():
    print("Hola " + Nombre + " ¡¡¡¡Bienvenido a la programación en Python!!!! ")      
saludar()

# Función para sumar números de forma dinámica
def suma_dinamica():
    print("\n--- Suma Dinámica ---")
    print("Ingresa números para sumarlos. Escribe 'salir' para detener.")
    
    total = 0
    contador = 0
    
    while True:
        try:
            entrada = input(f"Número {contador + 1}: ")
            
            # Verificar si el usuario quiere salir
            if entrada.lower() == 'salir':
                break
            
            # Convertir a número y sumar
            numero = int(entrada)
            total += numero
            contador += 1
            print(f"Suma actual: {total}")
            
        except ValueError:
            print("Error: Ingresa un número válido o 'salir' para terminar.")
    
    print(f"\nTotal de números ingresados: {contador}")
    print(f"Suma total: {total}")
    if contador > 0:
        promedio = total / contador
        print(f"Promedio: {promedio:.2f}")

# Ejecutar la suma dinámica
suma_dinamica()