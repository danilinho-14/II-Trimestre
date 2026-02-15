#Crie um jogo onde o computador sorteia um número e o usuário tenta adivinhar, tratando o máximo de erros possíveis.

from random import randint
from time import sleep

print("JOGO DA ADIVINHAÇÃO")
print("Vou pensar num número de 0 a 10 agora...\n")

while True:
    computador = randint(0, 10)
    sleep(1)

    while True:
        try:
            user = int(input("Tente adivinhar: "))
            if user < 0 or user > 10:
                print("Número inválido! Digite entre 0 e 10.")
                continue
            break
        except ValueError:
            print("Digite apenas números inteiros!")

    if user == computador:
        print("Acertaste!!")
    else:
        print(f"Erraste, pensei no número {computador}! HAHAHAHA")

    while True:
        cont = input("Vamos jogar mais? (s/n) ").strip().lower()
        if cont in ["s", "n"]:
            break
        print("Responda apenas 's' ou 'n'.")

    if cont == "n":
        print("Obrigado por jogar! Até à próxima.")
        break

