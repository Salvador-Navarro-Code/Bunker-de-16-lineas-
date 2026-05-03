import random

lista = ['piedra ', 'papel',  'tijera']

computadora = random.choice(lista)
jugador = None

while jugador not in lista:
	jugador = input("escoje entre piedra, papel o tijera ").lower()
	if jugador == computadora:
		print('computadora', computadora)
		print('jugador', jugador)
		print('Nadie gana carnal !')
	elif jugador == 'piedra':
		if computadora == 'papel':
		        print('computadora', computadora)
		        print('jugador', jugador)
		        print('Te la pelaste !')
		if computadora == 'tijera':
		        print('computadora', computadora)
		        print('jugador', jugador)
		        print(' A hu3vo me la pelaste !')
	elif jugador == 'papel':
		if computadora == 'tijera':
		        print('computadora', computadora)
		        print('jugador', jugador)
		        print('Te la pelaste !')
		if computadora == 'piedra':
		        print('computadora', computadora)
		        print('jugador', jugador)
		        print(' A hu3vo me la pelaste!')
		elif jugador == 'tijera':
		         if computadora == 'piedra':
		            print('computadora', computadora)
		            print('jugador', jugador)
		            print('Te la pelaste !')
		if computadora == 'papel':
		        print('computadora', computadora)
		        print('jugador', jugador)
		        print(' A hu3vo me la pelaste!')
