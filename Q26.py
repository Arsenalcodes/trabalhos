distancia_km = float(input("Digite a distância em quilômetros: "))
litros_gasolina = float(input("Digite a quantidade de litros de gasolina consumidos: "))
consumo = distancia_km / litros_gasolina
if consumo < 8:
    mensagem = "Venda o carro"
elif 8 <= consumo <= 14:
    mensagem = "Econômico"
else:
    mensagem = "Super econômico"
print(f"Consumo: {consumo:.2f} Km/l; mensagem: {mensagem}")