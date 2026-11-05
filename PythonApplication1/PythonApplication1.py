import random

# Загадываем случайное число от 1 до 10
secret_number = random.randint(1, 10)
attempts = 0

print("Я загадал число от 1 до 10. Попробуйте угадать!")

while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1

    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
        break
