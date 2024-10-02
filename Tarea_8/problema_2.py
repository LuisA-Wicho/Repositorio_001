print("\n\n\t\tS E R I E    F I B O N A C C I\n")

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

numero = int(input("Ingrese la posicion de la lista a buscar: "))

print(fibonacci(numero))