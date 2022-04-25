from time import sleep 
import string
class Usuario:
    num = None
    letras_abcdario = set(string.ascii_lowercase)
    def introduce_numero(self):
        
        try:
            sleep(0.3)
            self.num = int(input('¿cual es tu numero?:\n    '))
            sleep(0.3)
            
            if self.num < 1 or self.num > 10 :
                print("Este número no se encuentra entre el 0 al 10")
                sleep(0.3)

        except Exception as error:
            error_string = str(error)
            print(error_string)
            
        
        

