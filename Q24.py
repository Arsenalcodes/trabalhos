taxas_imposto = {
    "MG": 0.07, 
    "SP": 0.12,  
    "RJ": 0.15,  
    "MS": 0.08   
}
valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite o estado de destino (MG, SP, RJ, MS): ")

if estado_destino in taxas_imposto:
    taxa = taxas_imposto[estado_destino]
    preco_final = valor_produto + (valor_produto * taxa)
    print(f"O preço final do produto em {estado_destino} é R${preco_final:.2f}")
else:
    print("Erro: Estado de destino inválido.")