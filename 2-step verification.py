Email = input("cual es tu email?.").lower()
sms = input("ingresa el código recibido")
if"ejemplo@gmail.com" in Email and "1090670" in sms:
	print(" acceso concedido")
else: 
    print("por favor inténtalo de nuevo")
    print("El Email o el pin de acceso no coinciden")
  #En este breve ejercicio cree un autenticador de 2 pasos o un 2-step verification
