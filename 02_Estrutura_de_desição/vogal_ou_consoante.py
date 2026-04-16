letra = input("Digite uma letra do alfabeto: ").strip().lower()

vogais = ["a", "e", "i", "o", "u"]

if len(letra) != 1 or not letra.isalpha():
    print("Entrada inválida. Digite apenas uma única letra.")
elif letra in vogais:
    print("A sua letra é uma vogal!")
else:
    print("A sua letra é uma consoante!")
