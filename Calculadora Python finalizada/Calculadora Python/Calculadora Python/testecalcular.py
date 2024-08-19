from espaco import espaco
import time

class Calculadora:
        
    def calcular(self):
        
        print("\n\nBem vindo a calculadora, siga as instruções abaixo para começar a calcular.\n\n")
        time.sleep(1)
        
        # Solicitação de operador e validação
        operacao = input("Escolha o operador: \n\n Somar (+)\n Subtrair (-)\n Multiplicar (x)\n Dividir (/)\n\n Você escolheu: ").upper()
        if  operacao not in ('+', '-', 'X', '/'):
            print("\n\nVocê digitou um operador inválido, por favor, tente novamente.\n\n")
            self.calcular()
            return
        
        # Solicitação de números e validação
        while True:
            try:
                numero1 = float(input("\n\nDigite o primeiro número: "))
                numero2 = float(input("\nDigite o segundo número: "))
                break
            except ValueError:
                print("\n\nVocê digitou um número inválido, por favor, tente novamente.\n\n")
        
        # Execução da operação escolhida
        match operacao:
            case '+':
                resultado = numero1 + numero2
            case '-':
                while numero1 < numero2:
                    print("\n\nO primeiro número não pode ser menor que o segundo, por favor, tente novamente.\n\n")
                    time.sleep(1)
                    espaco()
                    self.calcular()
                    return
                resultado = numero1 - numero2
            case 'X':
                resultado = numero1 * numero2
            case _: # o que seria equivalente a case '/':m 
                while numero2 == 0:
                    print("\n\nNão pode dividir por 0, por favor, tente novamente.\n\n")
                    time.sleep(1)
                    espaco()
                    self.calcular()
                    return
                resultado = numero1 / numero2
        
        # if operacao == '+':
        #     resultado = numero1 + numero2
        # elif operacao == '-':
        #     while numero1 < numero2:
        #         print("\n\nO primeiro número não pode ser menor que o segundo, por favor, tente novamente.\n\n")
        #         time.sleep(1)
        #         espaco()
        #         self.calcular()
        #         return
        #     resultado = numero1 - numero2
        # elif operacao == 'X':
        #     resultado = numero1 * numero2
        # else:  # operacao == '/'
        #     while numero2 == 0:
        #         print("\n\nNão pode dividir por 0, por favor, tente novamente.\n\n")
        #         time.sleep(1)
        #         espaco()
        #         self.calcular()
        #         return
        #     resultado = numero1 / numero2
            
        espaco()
        print(f"\n\nO resultado é: {resultado}\n\n")
        espaco()

calculadora = Calculadora()
calculadora.calcular()
