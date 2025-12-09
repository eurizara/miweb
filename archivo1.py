##print("Hola mundo")
Nombre = input("Ingrese su nombre completo: ")
def saludar():
    print("Hola " + Nombre + " ¡¡¡¡Bienvenido a la programación en Python!!!! ")
    print("Sigue las instrucciones que se presentan a continuación.")
saludar()

import math

def leer_numero_o_salir(indice):
    """Lee una entrada del usuario y devuelve un float o la cadena 'salir'."""
    entrada = input(f"Número {indice} (o 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        return 'salir'
    try:
        # Permitimos números con decimales
        return float(entrada)
    except ValueError:
        print("Entrada inválida. Ingresa un número válido o 'salir'.")
        return None

def operar_dinamico(operacion):
    """Realiza la operación dinámica indicada por 'operacion'.
    operacion: 'sum', 'sub', 'mul', 'div'
    """
    nombres = {'sum': 'Suma', 'sub': 'Resta', 'mul': 'Multiplicación', 'div': 'División'}
    print(f"\n--- {nombres.get(operacion, 'Operación')} Dinámica ---")
    print("Ingresa números uno por uno. Escribe 'salir' para finalizar la operación.")

    numeros = []
    indice = 1
    while True:
        entrada = leer_numero_o_salir(indice)
        if entrada == 'salir':
            break
        if entrada is None:
            # entrada inválida; pedir de nuevo sin aumentar índice
            continue
        numeros.append(entrada)
        indice += 1

        # Calcular resultado parcial
        if operacion == 'sum':
            resultado = sum(numeros)
        elif operacion == 'mul':
            # usar math.prod si está disponible
            try:
                resultado = math.prod(numeros)
            except AttributeError:
                prod = 1
                for n in numeros:
                    prod *= n
                resultado = prod
        elif operacion == 'sub':
            if len(numeros) == 1:
                resultado = numeros[0]
            else:
                resultado = numeros[0]
                for n in numeros[1:]:
                    resultado -= n
        elif operacion == 'div':
            if len(numeros) == 1:
                resultado = numeros[0]
            else:
                resultado = numeros[0]
                for n in numeros[1:]:
                    if n == 0:
                        print("Aviso: se intentó dividir por cero; ese valor se ignora en el cálculo actual.")
                        continue
                    resultado /= n
        else:
            print("Operación no reconocida.")
            return

        print(f"Resultado parcial: {resultado}")

    # Mostrar resultado final
    if not numeros:
        print("No se ingresaron números. Operación cancelada.")
        return

    if operacion == 'sum':
        resultado_final = sum(numeros)
    elif operacion == 'mul':
        try:
            resultado_final = math.prod(numeros)
        except AttributeError:
            prod = 1
            for n in numeros:
                prod *= n
            resultado_final = prod
    elif operacion == 'sub':
        resultado_final = numeros[0]
        for n in numeros[1:]:
            resultado_final -= n
    elif operacion == 'div':
        resultado_final = numeros[0]
        for n in numeros[1:]:
            if n == 0:
                print("Aviso: se intentó dividir por cero; ese valor fue ignorado en el resultado final.")
                continue
            resultado_final /= n
    else:
        resultado_final = None

    print("\n--- Resultado Final ---")
    print(f"Cantidad de números ingresados: {len(numeros)}")
    print(f"Resultado: {resultado_final}")
    if operacion == 'sum' and len(numeros) > 0:
        promedio = sum(numeros) / len(numeros)
        print(f"Promedio: {promedio:.2f}")

def menu():
    while True:
        print("\n=== Menú de Operaciones Dinámicas ===")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Salir")
        opcion = input("Elige una opción (1-5): ")
        if opcion == '1':
            operar_dinamico('sum')
        elif opcion == '2':
            operar_dinamico('sub')
        elif opcion == '3':
            operar_dinamico('mul')
        elif opcion == '4':
            operar_dinamico('div')
        elif opcion == '5' or opcion.lower() == 'salir':
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Ingresa un número entre 1 y 5.")

if __name__ == '__main__':
    menu()