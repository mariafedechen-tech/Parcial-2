# Código de uma calculadora simples, que faz soma, subtração, multiplicação e divisão
# Para uma mais fácil comunicação com o usuário, vai ser dado um número para cada operação que a calculadora pode fazer
# O print está sendo usado para exibir essa mensagem para o usuário
print("Selecione a operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

# Vai ser pedido a pessoa que escolha o número referente a operação que ela quer realizar
# O input é usado para interpretar os números e no geral o que a pessoa digitar 
escolha = input("Digite o número da operação que deseja (1/2/3/4): ")

# Vai ser solicitado ao usuário para ele digitar os dois números que estarâo presentes na operação
# O float é usado para representar números quebrados 
# O input é usado para interpretar os números e no geral o que a pessoa digitar 
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Esses são os códigos bases para cada operação que a calculadora faz, a partir disso os valores dados pelo usuário só serão substituídos e o resultado será exibido para a pessoa
# O if é usado para dar uma condição, para caso a afirmação seja verdade
# O else é usado para quando de acordo com o if a afirmação for falsa
# O elif é uma abreviação do if e do else, ele permite que sejam testadas várias condições, nesse caso as 4 operações, sem que precise ficar usando todas as vezes o if e o else
  # O print é usado para mostrar o resultado do código
if escolha == '1':
    resultado = num1 + num2
    print(num1, "+", num2, "=", resultado)
elif escolha == '2':
    resultado = num1 - num2
    print(num1, "-", num2, "=", resultado)
elif escolha == '3':
    resultado = num1 * num2
    print(num1, "*", num2, "=", resultado)
elif escolha == '4':
    if num2 == 0:
        print("Erro! Divisão por zero.")
    else:
        resultado = num1 / num2
        print(num1, "/", num2, "=", resultado)

   
