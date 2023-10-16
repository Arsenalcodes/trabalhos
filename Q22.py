def verificar_aposentadoria(idade, tempo_servico):
    if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
        return "O trabalhador pode se aposentar."
    else:
        return "O trabalhador não pode se aposentar."
idade = int(input("Digite a idade do trabalhador: "))
tempo_servico = int(input("Digite o tempo de serviço do trabalhador (em anos): "))

resultado = verificar_aposentadoria(idade, tempo_servico)
print(resultado)