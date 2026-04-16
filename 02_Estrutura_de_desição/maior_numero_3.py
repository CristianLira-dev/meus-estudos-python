try:
    num1 = float(input("Digite o valor do primeiro número: "))
    num2 = float(input("Digite o valor do segundo número: "))
    num3 = float(input("Digite o valor do terceiro número: "))

    lista_numeros = [num1, num2, num3]
    maior_numero = max(lista_numeros)

    print(f"O maior número é: {maior_numero}")

except ValueError:
    print("Entrada inválida. Digite apenas números.")
