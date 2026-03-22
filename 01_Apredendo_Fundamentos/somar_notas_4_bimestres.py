Nota1 = float(input("Digite a nota do Primeiro Bimestre:  "))
Nota2 = float(input("\nDigite a nota do Segundo Bimestre:  "))
Nota3 = float(input("\nDigite a nota do Terceiro Bimestre:  "))
Nota4 = float(input("\nDigite a nota do Quarto Bimestre:  "))

media = (Nota1 + Nota2 + Nota3 + Nota4) / 4

if media > 6:
    passou_de_ano = True
else:
    passou_de_ano = False

print(f"\nAs Suas notas foram {Nota1}, {Nota2}, {Nota3} e {Nota4}  a sua média final foi {media}")

if (passou_de_ano):
    print("Parabens!! Passou de Ano!")
else:
    print("Infelizmente você não passou de ano :(")