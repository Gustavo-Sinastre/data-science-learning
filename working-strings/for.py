# Extraindo vogais de uma lista de palavras usando for
str_list = ['João', 'Roberto', 'Rafael']
letters = ["a", "e", "i", "o", "u"]
for name in str_list:
    for name_letters in name:
        if name_letters in letters:
            print(name_letters)


# Programa conta quantas letras ‘o’ ou ‘O’ tem em uma frase
frase = "Algoritmo e ProgramaçãO de Computadores I"
contLetra = 0
for c in frase:
    if c in "oO":
        print("Vogal: ", c)
        contLetra += 1
print("Total de letras o ou O: ", contLetra)
