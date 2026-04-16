import math
try:
    tamanho_MB = float(input("Digite o tamanho de um arquivo para download (em MB): "))
    velocidade_link = float(input("Digite a velocidade de um link de Internet (em Mbps):  "))

    megabits = tamanho_MB * 8
    tempo_em_segundos = megabits / velocidade_link
    velocidade_em_minutos = math.ceil(velocidade_em_segundos / 60)

    print(f"O tempo de download é {velocidade_em_minutos} minutos")

except ValueError:
    print("⚠️ Entrada inválida. Digite apenas números.")
