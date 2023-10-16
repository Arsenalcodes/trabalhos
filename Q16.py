import re
numero = input("Digite um número entre 1 e 12: ")

padroes = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abril',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}
if re.match(r'[1-12]', numero):
  
    mes = padroes[numero]
    print(f"O mês correspondente ao número {numero} é {mes}.")
else:
    print("Número fora do intervalo válido (1 a 12).")