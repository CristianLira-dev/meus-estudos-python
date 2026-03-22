hora_salario =  float(input("Digite o Valor da sua hora trabalhada: "))
horas_trabalhadas = int(input("\nDigite quantas horas voce trabalha por dia: "))
dias_trabalhados = int(input("\nQuantos dias voce trabalha por mes?: "))

valor_salario = (hora_salario * horas_trabalhadas) * dias_trabalhados

input(f"O seu salario mensal é de R$ {valor_salario}")