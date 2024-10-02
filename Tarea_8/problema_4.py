print("\n\n\t\tI N V E R T I R      C A D E N A         D E         T E X T O\n")

def invertir(ca):
    if len(ca) <= 1:
        return ca
    else:
        return ca[-1] + invertir(ca[:-1])
    

cadena = input("Ingrese el texto a invertir: ")

print(invertir(cadena))