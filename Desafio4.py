# Função para somar
def somar(x, y):
    return x + y

# Função para subtrair
def subtrair(x, y):
    return x - y

# Função para multiplicar
def multiplicar(x, y):
    return x * y

# Função para dividir
def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

# Menu da calculadora
def calculadora():
    print("Selecione a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    # Solicitar a escolha do usuário
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    # Verificar se a escolha é válida
    if escolha in ['1', '2', '3', '4']:
        # Solicitar os dois números
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            return
        
        # Realizar a operação com base na escolha
        if escolha == '1':
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Escolha inválida!")

# Chamar a função da calculadora
calculadora()
