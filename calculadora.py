print("- - - - - - - - - - - - - - - - -")
print("- - - C A L C U L A D O R A - - -")
print("- - - - - - - - - - - - - - - - -")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operacao = input("Escolha uma operação(+, -, x, /): ")

if operacao == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif operacao == "-":
    print(f"{n1} - {n2} = {n1-n2}")
elif operacao == "*":
    print(f"{n1} x {n2} = {n1 * n2}")
elif operacao == "/":
    if n2 != 0:
        print(f"{n1} / {n2} = {n1/n2}")
    else:
        print("Não é possível dividir por zero!")
else:
    print("Operação inválida!")