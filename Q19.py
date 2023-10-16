numero = int(input("Digite um número inteiro: "))
if (numero % 3 == 0 or numero % 5 == 0) and not (numero % 3 == 0 and numero % 5 == 0):
    print(f"O número {numero} é divisível por 3 ou 5, mas não por ambos ao mesmo tempo.")
else:
    print(f"O número {numero} não atende aos critérios especificados.")