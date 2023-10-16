import re
numero = input("Digite um número entre 1 e 7: ")

padroes = {
    '1': 'Domingo',
    '2': 'Segunda-feira',
    '3': 'Terça-feira',
    '4': 'Quarta-feira',
    '5': 'Quinta-feira',
    '6': 'Sexta-feira',
    '7': 'Sábado'
}
if re.match(r'[1-7]', numero):
  
    dia_semana = padroes[numero]
    print(f"O dia da semana correspondente ao número {numero} é {dia_semana}.")
else:
    print("Número fora do intervalo válido (1 a 7).")
