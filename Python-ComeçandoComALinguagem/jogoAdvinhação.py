import random

print("-" * 20, "Jogo de advinhação!", "-" * 20)
numeroSorteado = random.randrange(1, 11)
print("Você possui 3 chances para acertar um número de 1 até 10.")
chute = int(input("Qual número você deseja chutar primeiro??\n"))

i = 1
while chute != numeroSorteado and i < 3:
    chute = int(input("Qual número deseja chutar agora?\n"))
    i += 1
if chute != numeroSorteado:
    print("Não foi dessa vez. Tente novamente mais tarde.\n")
elif chute == numeroSorteado:
    print("Parabéns! Você acertou o número sorteado!\n")
else:
    print("Dados inválidos.\n")

print("Programa finalizado.")
