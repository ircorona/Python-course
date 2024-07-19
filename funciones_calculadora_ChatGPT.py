def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

def get_numbers():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada no válida. Por favor, ingrese números válidos.")

def calculator():
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        option = input("Ingrese su opción (1, 2, 3, 4, 5): ")

        if option == "5":
            print("Saliendo de la calculadora.")
            break

        if option in ["1", "2", "3", "4"]:
            num1, num2 = get_numbers()

            if option == "1":
                print("La suma es:", add(num1, num2))
            elif option == "2":
                print("La resta es:", subtract(num1, num2))
            elif option == "3":
                print("La multiplicación es:", multiply(num1, num2))
            elif option == "4":
                result = divide(num1, num2)
                print("La división es:", result)
        else:
            print("Opción no válida, intenta de nuevo.")

calculator()
