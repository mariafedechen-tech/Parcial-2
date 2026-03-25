# operação básica para soma
def somar(x, y):
    return x + y

# Operação básica para subtrair
def subtrair(x, y):
    return x - y

# operação básica para multiplicar
def multiplicar(x, y):
    return x * y

# Operação básica para divisão
def dividir(x, y):
    if y == 0:
        return "Erro! Esta é uma divião por zero."
    else:
        return x / y

# Estas são as possíveis operações que a calculadora simples pode executar
def calculadora():
    print("Selecione a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    # Peça para o usuário que escolha qual operação ele quer fazer
    escolha = input("escreva o número de acordo com a operação que você deseja (1/2/3/4): ")

    # Será verificado qual operação o usuário escreveu
    if escolha in ['1', '2', '3', '4']:
        # Agora que já sabemos a operação, peça ao usuário que digite os dois números para a operação
        try:
            num1 = float(input("Escreva o primeiro número: "))
            num2 = float(input("Escreva o segundo número: "))
       
        
        # Agora será feita a operação de acordo com o que a pessoa escolheu
        if escolha == '1':
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
    # Se a pessoa escolher algo que não está programado para a calculdora fazer será mandado a mensagem que escolha inválida
    else:
        print("Escolha inválida!")

# Chamar a função da calculadora
calculadora()
