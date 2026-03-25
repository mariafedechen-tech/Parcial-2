# Código para calcular os juros simples
# Será pedido ao usuário que digite o valor desejado para cada elemento: capital, taxa e o tempo

capital = float(input("Escreva o valor do capital: "))
taxa = float(input("Escreva a taxa (%): "))
tempo = float(input("Escreva o tempo em anos: "))
 # Esta é a fórmula dos juros simples, os dados digitados pelo usuário vão ser substituidos na fórmula
juros = (capital * taxa * tempo) / 100

# O resultado vai ser exibido para o usuário
print("O valor dos juros é:", juros)

