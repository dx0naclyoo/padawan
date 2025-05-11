import random

choices = ["камень", "ножницы", "бумага"]
player = input("Сделай ход (камень, ножницы, бумага): ").lower()
computer = random.choice(choices)

print(f"Компьютер выбрал: {computer}")

if player == computer:
    print("Ничья!")
elif (
    (player == "камень" and computer == "ножницы") or
    (player == "ножницы" and computer == "бумага") or
    (player == "бумага" and computer == "камень")
):
    print("Победил: ты!")
else:
    print("Победил: компьютер")