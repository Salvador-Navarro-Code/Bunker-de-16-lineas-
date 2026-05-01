password = input("cual es la contraseña?.")
if"05Dsm/90" in password:
	print(" por favor ingrese el numero que le llegara via sms.")
else:
	print("La contraseña no coincide")
	second_attempt = input("Le quedan 2 intentos para poner la contraseña")
	if"05Dsm/90" in second_attempt:
		print("Bienvenido")
	else:
			print("La contraseña sigue sincoincidir")
	third_attempt = input("este es su ultimo intento")
	if"05Dsm/90" in third_attempt:
		print("Bienvenido justo en el ultimo intento")
	else:
			print("se mando un correo electronico para restablecer tu cuenta")
			print("por motivos de seguridad tu usuario fue bloqueado por multibles intentos erróneos")
			#No es mucho pero es trabajo honesto 
