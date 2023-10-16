def soma(a, b):
    return a + b

def diferenca(a, b):
    return abs(a - b)

def produto(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

opcao = input("Opção: ")

if opcao == "1":
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = soma(a, b)
    print(f"Resultado da soma: {resultado}")
elif opcao == "2":
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = diferenca(a, b)
    print(f"Resultado da diferença: {resultado}")
elif opcao == "3":
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = produto(a, b)
    print(f"Resultado do produto: {resultado}")
elif opcao == "4":
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número (não pode ser zero): "))
    resultado = divisao(a, b)
    print(f"Resultado da divisão: {resultado}")
else:
    print("Opção inválida. Escolha uma opção válida de 1 a 4.")