try:
    numero1 = float(input("Digite o Primeiro número:  "))
    numero2 = float(input("Digite o Segundo número:  "))

    if numero1 > numero2:
     print(f"O maior número é o {numero1}")
    elif numero2 > numero1:
     print(f"O maior número é o {numero2}")
    else:
       print("Os Números são iguais")

except ValueError:
    print("⚠️ Entrada inválida. Digite apenas números.")