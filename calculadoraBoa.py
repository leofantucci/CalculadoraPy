import os

def soma(x,y):
    return (x+y)
    
def subtracao(x,y): 
    return (x-y)

def divisao(x,y):
    return (x/y)
def multiplicacao(x,y): 
    return (x*y)

def potencia(x,y):
   return (x^y)

def raiz(x,y):
    return(x ** (1/y))

operacao = 100
while(True):
    input("Aperte ENTER para iniciar...")
    os.system('clear')

    print("Escolha o tipo de operação desejado: ")
    print("Soma (0)")
    print("Subtração (1)")
    print("Divisão (2)")
    print("Multiplicação - (3)")
    print("Potenciação - (4)")
    print("Raiz quadrada - (5)")
    print("SAIR - (99)")

    operacao = int(input())
    if(operacao == 99):
       break
    elif(operacao > 5 or operacao < 0):
        print("INSIRA UM NUMERO VÁLIDO")
    else:
        x = int(input("Insira o 1° numero: "))
        y = int(input("Insira o 2° numero: "))

        res = 0

        os.system('clear')

        if operacao == 0:
            print("===========SOMA===========")
            print("----RESULTADO = X + Y-----")
            print("==========================")
            res = soma(x,y)
        elif operacao == 1:
            print("========SUBTRAÇÃO========")
            print("----RESULTADO = X - Y----")
            print("=========================")
            res = subtracao(x,y)
        elif operacao == 2:
            print("==========DIVISÃO==========")
            print("-----RESULTADO = X / Y-----")
            print("===========================")
            res = divisao(x,y)
        elif operacao == 3:
            print("==========MULTIPLICAÇÃO==========")
            print("--------RESULTADO = X * Y--------")
            print("=================================")
            res = multiplicacao(x,y)
        elif operacao == 4:
            print("==========POTENCIAÇÃO==========")
            print("-------RESULTADO = X ^ Y-------")
            print("===============================")
            res = potencia(x,y)
        elif operacao == 5:
            print("=========RAIZ QUADRADA=========")
            print("----RESULTADO = sqrt(x, y)-----")
            print("===============================")
            res = raiz(x,y)

        print("Resultado: " + str(res))
