# Código que converte um número de segundos para horas, minutos e segundos
# Outro código depois que irá fazer o contrário
segundos = int(input("escreva a quantidade de segundos"))
minutos  = (segundos//60)
horas    = (segundos//3600)

print("esse número de segundos tem como resultado", horas, "horas","ou" minutos, "minutos e ainda", segundos, "segundos")

# Será feito o contrário agora, para isso será pedido para o usuário escrever uma quantidade de horas
h = int(input( "escreva quantas horas"))
seg = ( h * 3600 )
m = ( h * 60 ) 
print("esse número de horas tem como resultado", h, "horas", "ou", m, "minutos e ainda", seg, "segundos")
   
