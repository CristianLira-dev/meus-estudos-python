import math

try:
    area = float(input("Informe o tamanho em m² da área a ser pintada: "))

    litros_necessarios = area / 3
    latas = math.ceil(litros_necessarios / 18)
    valor_final = latas * 80

    print(f"\nLitros necessários: {litros_necessarios:.2f} L")
    print(f"Latas a comprar: {latas}")
    print(f"Preço total: R$ {valor_final:.2f}\n")

except ValueError:
    print("⚠️ Entrada inválida. Digite apenas números.")
