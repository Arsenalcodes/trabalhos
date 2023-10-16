trabalho_lab = float(input("Nota do Trabalho de Laboratório (0 a 10): "))
avaliacao_semestral = float(input("Nota da Avaliação Semestral (0 a 10): "))
exame_final = float(input("Nota do Exame Final (0 a 10): "))

if 0 <= trabalho_lab <= 10 and 0 <= avaliacao_semestral <= 10 and 0 <= exame_final <= 10:
    
    media_final = (trabalho_lab * 2 + avaliacao_semestral * 3 + exame_final * 5) / 10

    
    if 0 <= media_final < 3:
        situacao = "Reprovado"
    elif 3 <= media_final < 5:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"

    print(f"Nota Final: {media_final:.2f} - Situação: {situacao}")
else:
    print("Notas fora do intervalo válido (0 a 10).")