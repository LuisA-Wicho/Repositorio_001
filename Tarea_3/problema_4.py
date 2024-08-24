ano = int(input("Introdusca el año de nacimiento: "))
mes = int(input("Introdusca el mes de nacimiento: "))
dia = int(input("Introdusca el dia de nacimiento: "))

print("Considerando que hoy es 23/08/2024 y que los meses duran ")

calano = 2024 - ano
calmes = 8 - mes
caldia = 23 - dia

cantano = (12 + calmes) // 12
cantmes = (12 + calmes) % 12

cantdia = (calano * 365) + (calmes * 30) + (caldia)

print("La cantidad de dias que han pasado es: ", cantdia)