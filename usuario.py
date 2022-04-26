class Usuario:
    num = None
    def introduce_numero(self):
        self.num = None
        while self.num == None:
            try:
                self.num = int(input('¿cual es tu numero?:\n    '))
            except Exception as error:
                error_string = str(error)
                print(error_string)
                continue;      
            
            if self.num < 1:
                self.num = None
                print("Este número NO se encuentra entre el 1 al 10. Este número es menor de 1.")
            
            elif self.num > 10:
                self.num = None
                print("Este número NO se encuentra entre el 1 al 10. Este número es mayor de 10.")
