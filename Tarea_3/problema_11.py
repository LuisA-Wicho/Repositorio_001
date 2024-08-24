peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / altura ** 2

print("Su IMC es de: {:.2f}".format(imc))