# Código que converte um número de segundos para horas, minutos e segundos
# Outro código depois que irá fazer o contrário
# O int é usado para números inteiros
# o input é usado para interpretar os números e no geral o que a pessoa digitar 
segundos = int(input("escreva a quantidade de segundos: "))
minutos  = (segundos//60)
horas    = (segundos//3600)

# Será mostrado o resultado
# O print é usado para mostrar o resultado do código
print("horas:")
print(horas)
print("minutos:")
print(minutos)
print("segundos:")
print(segundos)

# Será feito o contrário agora, para isso será pedido para o usuário escrever uma quantidade de horas
# O int é usado para números inteiros
# o input é usado para interpretar os números e no geral o que a pessoa digitar 
h = int(input( "escreva quantas horas: "))
seg = ( h * 3600 )
m = ( h * 60 ) 
# Será mostrado o resultado
# O print é usado para mostrar o resultado do código
print("horas:")
print(h)
print("minutos:")
print(m)
print("segundos:")
print(seg)
   
