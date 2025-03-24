while True:
    try:

        input_number = input("Por favor, digite um número par: ").replace(",",".")
        number = float(input_number)

        if number.is_integer():
            number = int(number)
            if number % 2 == 0:
                print("✅ Parabéns! O número é par!")
                break
            else:
                print("❌ O número digitado não é par!")
        else:
            print("⚠️ Por favor, digite um número inteiro, não decimal!")

    except ValueError:
        print("❗ Entrada inválida! Digite apenas números.")