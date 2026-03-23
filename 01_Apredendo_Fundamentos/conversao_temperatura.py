print("\n\n---------- Conversão de Temperaturas ----------")

temperatura_escolhida = input("\nDeseja fazer a conversão para Celsius ou Fahrenheit? (Digite 'C' para Celcisius e 'F' para Fahrenheit) ").upper()

if temperatura_escolhida == "F":
    fahrenheit_temperatura = float(input("\nDigite a Temperatura em Fahrenheit:  "))
    fahrenheit_convertida = (fahrenheit_temperatura - 32) / 1.8
    fahrenheit_arredondada = round(fahrenheit_convertida, 2)
    print(f"\nA temperatura era {fahrenheit_temperatura}°F e ficou {fahrenheit_arredondada}°C")
elif temperatura_escolhida == "C":
    celsius_temperatura = float(input("\nDigite a Temperatura em Celsius:  " ))
    celsius_convertida = (celsius_temperatura * 1.8) + 32
    celsius_arredondada = round(celsius_convertida, 2)
    print(f"\nA temperatura era {celsius_temperatura}°C e ficou {celsius_arredondada}°F")
else:
    print("\nEscolha errada Seleciona 'C' ou 'F' para fazer a conversão")
    

