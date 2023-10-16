# Solicita o peso e a altura da pessoa
peso = float(input("Digite o peso (em quilogramas): "))
altura = float(input("Digite a altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o IMC
print(f"Seu IMC é: {imc:.2f}")

# Determina a classificação com base no IMC
classificacao = ""
if imc < 18.5:
    classificacao = "Abaixo do Peso"
elif 18.5 <= imc < 25.0:
    classificacao = "Saudável"
elif 25.0 <= imc < 30.0:
    classificacao = "Peso em Excesso"
elif 30.0 <= imc < 35.0:
    classificacao = "Obesidade Grau I"
elif 35.0 <= imc < 40.0:
    classificacao = "Obesidade Grau II (severa)"
else:
    classificacao = "Obesidade Grau III (mórbida)"

# Exibe a classificação
print(f"Sua classificação é: {classificacao}")
