
class Calculadora:

    def somar(self, a, b):
        return f"{a} + {b} = {a+b}"
    
    def subtrair(self, a, b):
        return f"{a} - {b} = {a-b}"
    
    def multiplicar(self, a, b):
        return f"{a} x {b} = {a*b}"
    
    def dividir(self, a, b):
        if b != 0:
            return f"{a} / {b} = {a/b}"
        else:
            mensagem = "Não é possível dividir por zero!"
            return mensagem
        
    def mostrar_menu(self):
        print("=" * 30)
        print("=== C A L C U L A D O R A ====")
        print("=" * 30)
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")
        print("=" * 30)

calc = Calculadora()

while True:

    calc.mostrar_menu()

    operacao = int(input("Escolha uma das opções acima: "))

    if operacao == 0:
        break

    if operacao not in [1,2,3,4]:
        print("Operação inválida!")
        continue

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if operacao == 1:
        print(calc.somar(n1, n2))
    elif operacao == 2:
        print(calc.subtrair(n1, n2))
    elif operacao == 3:
        print(calc.multiplicar(n1, n2))
    elif operacao == 4:
        print(calc.dividir(n1, n2))
            

print("=" * 30)
print("Obrigado por usar a calculadora!  :)")
print("=" * 30)

