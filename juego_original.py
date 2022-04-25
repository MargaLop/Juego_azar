import random

numero_azar = random.randint(1,10)



while(True):
    numero_usuario= int(input('¿cual es tu numero?:'))

    if numero_azar < numero_usuario:
        print('más bajo')
    elif numero_azar > numero_usuario:
        print('más alto')
    else:
        print('ACERTASTE')
        break


