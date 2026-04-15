hora_salario =  float(input("Digite o Valor da sua hora trabalhada: "))
horas_trabalhadas = int(input("\nDigite quantas horas voce trabalha por mes:"))

valor_salario = (hora_salario * horas_trabalhadas)

salario_imposto_de_renda = valor_salario * 0.11
salario_inss = valor_salario * 0.08
salario_sindicato = valor_salario * 0.05
descontos = salario_imposto_de_renda + salario_inss + salario_sindicato
salario_liquido = valor_salario - descontos

print("\nFolha de pagamento:")
print(f"+ Salário Bruto : R$ {valor_salario:.2f}")
print(f"- Imposto de Renda (11%)      : R$ {salario_imposto_de_renda:.2f}")
print(f"- INSS (8%)     : R$ {salario_inss:.2f}")
print(f"- Sindicato (5%): R$ {salario_sindicato:.2f}")
print(f"= Salário Líquido: R$ {salario_liquido:.2f}")