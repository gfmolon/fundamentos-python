import random

while True:
    opiniao = int(input("Informe o lado que o dado vai cair: "))

    jogada = random.randint(1, 6)

    print(f"Computador: {jogada}")
    print(f"Você: {opiniao}")

    if opiniao == jogada:
        print("Que sorte! O dado caiu exatamente no que você disse!")
        break
    else:
        print("Continue tentando.")
