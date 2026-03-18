# Função para calcular os juros simples
def calcular_juros_simples(capital, taxa, tempo):
    juros = (capital * taxa * tempo) / 100
    return juros

# Solicitar ao usuário os valores de capital, taxa e tempo
def calcular_juros():
    try:
        # Entrada de dados
        capital = float(input("Digite o valor do capital (C): "))
        taxa = float(input("Digite a taxa de juros (I) em %: "))
        tempo = float(input("Digite o tempo (T) em anos: "))
        
        # Calcular os juros
        juros = calcular_juros_simples(capital, taxa, tempo)
        
        # Exibir o resultado
        print(f"O valor dos juros é: R${juros:.2f}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Chamar a função para calcular os juros
calcular_juros()
