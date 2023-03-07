import random
import string
import re

patron = re.compile(r'[^A-Za-z0-9\s]')

def generador_contraseña():
    Longitud = int(input("Ingrese Longitud de contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        contraseña = ''.join(random.choice(caracteres) for i in range(Longitud))
        if (any(c.islower() for c in contraseña)
            and any(c.isupper() for c in contraseña)
            and sum(c.isdigit() for c in contraseña) >= 2
            and any(c in string.punctuation for c in contraseña)):
            break
    return contraseña
    #contraseña = generador_contraseña()
    #print("\nLa contraseña generada es:" ,contraseña)





def validar_contraseña(contraseña):
    if len(contraseña) <= 8:
      print("\nLa contraseña no contiene la cantidad de caracteres necesarios.")
      return False

    if not patron.search(contraseña):
      print("\nLa contraseña no contiene un caracter especial.")
      return False
      
    if not re.search(r'[A-Z]', contraseña):
      print("\nLa contraseña no contiene al menos una letra mayuscula.")
      return False
      
    if not re.search(r'[a-z]', contraseña):
      print("\nLa contraseña no contiene al menos una letra minuscula.")
      return False
      
    if not re.search(r'[0-9]', contraseña):
      print("\nLa contraseña no contiene al menos un numero.")
      return False
      
    return True
  
def main():
  print("    Generador y Validador de contraseña\n")
  print("Ingrese el numero 1 si desea generar una contraseña\nIngrese el numero 2 si desea validar una contraseña")
  Menu = int(input("\nIngrese la opcion deseada:"))
  if Menu == 1:
    contraseña = generador_contraseña()
    print("\nLa contraseña generada es:" ,contraseña)
   
  elif Menu == 2:
    contraseña = (input("Ingresa tu contraseña:"))
    #validar_contraseña(contraseña)

    if validar_contraseña(contraseña):
      print("\n La contraseña es válida")
    else:
      print("\n La contraseña es inválida")
  else:
    print("La opcion seleccionada no es correcta")

main()