import string
class Usuario:
    num = None
    letras_abcdario = set(string.ascii_lowercase)
    def introduce_numero(self):
        while self.num == None:
            try:
                self.num = int(input('¿cual es tu numero?:\n    '))
            except Exception as error:
                error_string = str(error)
                print(error_string)
                continue;                
            
            if self.num < 1:
                print("Este número NO se encuentra entre el 1 al 10. Este número es menor de 1.")
            
            elif self.num > 10:
                print("Este número NO se encuentra entre el 1 al 10. Este número es mayor de 10.")




