print("\n\n\t\tF A C T O R I A L\n")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un numero entero: "))

print(factorial(numero))
