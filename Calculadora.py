# funciones de operacion
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Error: División por cero"

def calculadora():
    print("--- Calculadora Básica Python ---")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
    
    while True:
        try:
            opcion = input("Seleccione opción (1-5): ")
            
            if opcion == '5':
                print("¡Gracias por usar la calculadora!")
                break
                
            num1 = float(input("Ingrese primer número: "))
            num2 = float(input("Ingrese segundo número: "))
            
            if opcion == '1': print("Resultado:", sumar(num1, num2))
            elif opcion == '2': print("Resultado:", restar(num1, num2))
            elif opcion == '3': print("Resultado:", multiplicar(num1, num2))
            elif opcion == '4': print("Resultado:", dividir(num1, num2))
            else: print("Opción no válida")
            
        except ValueError:
            print("Error: Ingrese números válidos")

if __name__ == "__main__":
    calculadora()
