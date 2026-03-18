# Função para calcular a área do triângulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# Solicitar ao usuário a base e a altura do triângulo
def calcular_area():
    try:
        base = float(input("Digite o valor da base do triângulo: "))
        altura = float(input("Digite o valor da altura do triângulo: "))
        
        # Calcular a área
        area = area_triangulo(base, altura)
        
        # Exibir o resultado
        print(f"A área do triângulo com base {base} e altura {altura} é: {area}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Chamar a função para calcular a área
calcular_area()
