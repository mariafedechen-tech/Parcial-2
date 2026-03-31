# Código para verificar se um número é par
# Vai ser pedido para o usuário digitar algum número
# O int é usado para números inteiros
# o input é usado para interpretar os números e no geral o que a pessoa digitar 
numero = int(input("Digite um número: "))
# Será verificado se o número digitado pelo usuário é par
# O if é usado para dar uma condição, para caso a afirmação seja verdade
if numero % 2 == 0:
  # A resposta vai ser apresentada
  # O print é usado para mostrar o resultado do código
     print('número par') 
  # O else é usado para quando de acordo com o if a afirmação for falsa
# O print é usado para mostrar o resultado do código
else: 
     print('número ímpar')
