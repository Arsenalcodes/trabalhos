def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("Escolha uma operação matemática:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite o número da operação desejada: ")

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

if escolha == "1":
    resultado = soma(a, b)
    operacao = "soma"
elif escolha == "2":
    resultado = subtracao(a, b)
    operacao = "subtração"
elif escolha == "3":
    resultado = multiplicacao(a, b)
    operacao = "multiplicação"
elif escolha == "4":
    resultado = divisao(a, b)
    operacao = "divisão"
else:
    resultado = "Operação inválida"
    operacao = ""

print(f"Resultado da {operacao}: {resultado}")