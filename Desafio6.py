# Função para converter segundos em horas, minutos e segundos
def converter_para_hms(segundos):
    horas = segundos // 3600  # 1 hora tem 3600 segundos
    minutos = (segundos % 3600) // 60  # Resto da divisão por 3600 dividido por 60 (minutos)
    segundos_restantes = segundos % 60  # Resto da divisão por 60 (segundos restantes)

    return horas, minutos, segundos_restantes

# Solicitar ao usuário o número de segundos
def converter_segundos():
    try:
        segundos = int(input("Digite o número de segundos: "))
        
        # Converter e exibir o resultado
        horas, minutos, segundos_restantes = converter_para_hms(segundos)
        print(f"{segundos} segundos é igual a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
    
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# Chamar a função de conversão
converter_segundos()
