print("\n\n\t\tP O T E N C I A\n")

def potencia(x,y):
    if y == 0:
        return 1
    else:
        return x * potencia(x,y-1)

a = int(input("Ingrese el numero base: "))
b = int(input("Ingrese el numero potencia: "))

print(potencia(a,b))