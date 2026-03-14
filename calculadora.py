def somar(a, b):
        return f"{a} + {b} = {a+b}"
    
def subtrair(a, b):
    return f"{a} - {b} = {a-b}"
    
def multiplicar(a, b):
    return f"{a} * {b} = {a*b}"
    
def dividir(a, b):
    if b != 0:
        return f"{a} / {b} = {a/b}"
    else:
        return "Não é possível dividir por zero!"


while True:

    print("- - - - - - - - - - - - - - - - -")
    print("- - - C A L C U L A D O R A - - -")
    print("- - - - - - - - - - - - - - - - -")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    print("- - - - - - - - - - - - - - - - - ")

    operacao = int(input("Escolha uma das opções acima: "))

    if operacao == 0:
        break

    if operacao not in [1,2,3,4]:
        print("Operação inválida!")
        continue

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if operacao == 1:
        print(somar(n1, n2))
    elif operacao == 2:
        print(subtrair(n1, n2))
    elif operacao == 3:
        print(multiplicar(n1, n2))
    elif operacao == 4:
        print(dividir(n1, n2))
        

print("=" * 30)
print("Obrigado por usar a calculadora!  :)")
print("=" * 30)