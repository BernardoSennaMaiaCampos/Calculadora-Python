from espaco import espaco
import time

class Calculadora:
        
    def calcular(self):
        
        print("\n\nBem vindo a calculadora, siga as instruções abaixo para começar a calcular.\n\n")
        time.sleep(1)
        operacao = input("Escolha o operador: \n\n Somar (+)\n Subtrair (-)\n Multiplicar (x)\n Dividir (/)\n\n Você escolheu: ").upper()

        def somar():
            return numero1 + numero2

        def subtrair():
            while numero1 < numero2:
                print("\n\nO primeiro número não pode ser menor que o segundo, por favor, tente novamente.\n\n")
                time.sleep(1)
                espaco()
                self.calcular(self)
                break
            else:
                return numero1 - numero2

        def multiplicar():
            return numero1 * numero2

        def dividir():
            while numero2 == 0:
                print("\n\nNão pode dividir por 0, por favor, tente novamente.\n\n")
                time.sleep(1)
                espaco()
                self.calcular(self)
                break
            else:
                return numero1 / numero2
            
        numero1 = float(input("\n\nDigite o primeiro número: "))
        numero2 = float(input("\nDigite o segundo número: "))
        
        resultado = None

        match operacao:
            case "+":
                resultado = somar()
            case "-":
                resultado = subtrair()
            case "X":
                resultado = multiplicar()
            case "/":
                resultado = dividir()
            case _:
                print("\n\nVocê digitou errado o operador, tente novamente.\n\n")
                espaco()
                self.calcular()
                return
        espaco()
        print(f"\n\nO resultado é: {resultado}\n\n")
        espaco()

calculadora = Calculadora()
calculadora.calcular()


