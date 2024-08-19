from testecalcular import Calculadora
from espaco import espaco

def Jogarnovamente():
    jogarnovamente = input("\n\nVocê deseja calcular novamente? (Y/y) para sim, (N/n) para não: \n\nVocê escolheu: ").upper()
    espaco()
    match jogarnovamente:
        case "Y":
          Calculadora.calcular(self=Calculadora)
        case "N":
            print("\n\nO programa se encerrou.\n\n")
            return False
        case _:
            print("\n\nVocê digitou errado, tente novamente.\n\n")

