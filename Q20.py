A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

if A < B + C and B < A + C and C < A + B:
    if A == B == C:
        tipo = "Equilátero"
    elif A == B or A == C or B == C:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    
    print(f"Os valores {A}, {B} e {C} formam um triângulo {tipo}.")
else:
    print("Os valores não podem formar um triângulo.")