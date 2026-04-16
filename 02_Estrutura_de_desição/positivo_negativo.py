try:
    numero = float(input("Digite um número:  "))

    if numero > 0:
     print(f"O número é positivo")
    elif numero < 0:
     print(f"O número é negativo")
    else:
       print("O Seu número é 0")

except ValueError:
    print("⚠️ Entrada inválida. Digite apenas números.")