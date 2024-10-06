print("\n\n\t\tS U M A      D E         D I G I T O S\n")

def suma(n):
    if n < 10:
        return n
    else:
        return ((n / 10) - (n // 10)) * 10 + suma(n // 10)

numero = int(input("Ingrese el numero a sumar sus digitos: "))

print(suma(numero))
