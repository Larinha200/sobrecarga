# padrão 
class Calculadora:
    def soma(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculadora()
print(calc.soma(2, 3))      # Soma dois números
print(calc.soma(2, 3, 4))   # Soma três números
print(calc.soma(5))         # Soma apenas um número
