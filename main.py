# from juego import Juego
from random import randint

class Usuario:
    num = None
    def introduce_numero(self):
        self.num = int(input('¿cual es tu numero?:\n    '))


class Juego:
    num = None
    usuario = None

    def __init__(self):
        self.num = randint(1,10)
        self.usuario = Usuario()
    
    def juega(self):
        while(self.usuario.num != self.num):
            self.usuario.introduce_numero()
            if self.num < self.usuario.num:
                print('más bajo')
            elif self.num > self.usuario.num:
                print('más alto')
            else:
                self.victoria() 
                
        
    def victoria(self):
        print('ACERTASTE')
              




if __name__ == '__main__':
    juego = Juego()
    juego.juega()

    usuario = Usuario()
