# Esta é a fórmula da área do triângulo que vai ser usada 
def area_triangulo(base, altura):
    return (base * altura) / 2

# Vai ser pedido ao usuário para que ele digite os valore para a base e a altura do triângulo
def calcular_area():
    try:
        base = float(input("Escreva o valor deejado para a base do triângulo: "))
        altura = float(input("Escreva o valor desejado para a altura do triângulo: "))
        
        # Agora que temos os valores, vai ser calculado de acordo com a fórmula a área do triãngulo
        area = area_triangulo(base, altura)
        
        # O resultado da conta vai ser apresentado
        print(f"A área do triângulo com base {base} e altura {altura} é: {area}")
    
    
# Chamar a função para calcular a área
calcular_area()
