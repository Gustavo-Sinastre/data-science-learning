# Exercício para transformar a temperatura em ºC para ºF

# Input das informações
input_data = input("Informe a temperatura em ºC: ").replace(",", ".")

# Verficando se o input é um número
try:
    initial_data = float(input_data)
    print("O input digitado é um número, iniciando conversão...")
except ValueError:
    initial_data = ""
    print("É necessário um número para conversão.")

if initial_data != "":
    fahrenheit = round(((1.8 * initial_data) + 32),2)
    print(f"A temperatura em º foi {input_data} ºC")
    print(f"O valor convertido é {fahrenheit} ºF")
else:
    print("Fechando o programa...")