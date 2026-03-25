# Código que converte um número de segundos para horas, minutos e segundos
# Outro código depois que irá fazer o contrário
segundos = int(input("escreva a quantidade de segundos))
minutos  = (segundos/60)
horas    = (segundos/3600)

print("esse número de segundos tem como resultado", horas, "horas","ou" minutos, "minutos e ainda", segundos, "segundos")

# Peça ao usuário que escreva o número em segundos
def converter_segundos():
    try:
        segundos = int(input("Digite o número de segundos: "))
        
        # O número escrito vai ser convertido e o resultado vai ser exibido
        horas, minutos, segundos_restantes = converter_para_segundos
        print(f"{segundos} segundos é igual a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
   
