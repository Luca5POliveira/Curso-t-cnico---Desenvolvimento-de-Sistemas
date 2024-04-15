while True:
    print("------------- CHOICES ------------------\n"
            "OPCÔES:\n"
            "Digite 1 para contar de 1 ate 10. \n"
            "Digite 2 para contar de 1 até o numero que desejar.\n"
            "Digite 3 para mostrar a sequencia de números primos\n"
            "Digite 'parar' para encerar o programa ou Qualquer tecla parar continuar\n"
            "----------------------------------------")

    escolha = input("R - ")
    if escolha == "1":
        for i in range (1,11):
            print(i)

    elif escolha == "2":
        numero = int(input("Até que numero você quer ver?: "))
        for i in range (1, numero + 1):
            print(i)

    elif escolha == "3":
        numeroP = int(input("Até que numero você quer ver?: "))
        for i in range (1, numeroP+1):
            if(numeroP % i == 0):
                print(i)

    elif escolha == "parar":
        break