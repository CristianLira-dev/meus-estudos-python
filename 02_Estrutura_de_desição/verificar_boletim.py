try:
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))

    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
        print(" As notas devem estar entre 0 e 10.")
    else:
        media = (nota1 + nota2) / 2

        if media >= 7:
            print(f"Parabéns! Você foi aprovado com média {media:.2f}.")
        else:
            print(f"Você não atingiu a média necessária. Média: {media:.2f}.")

except ValueError:
    print("Entrada inválida. Digite apenas números.")
