from datetime import datetime

name = input("Введите ваше имя: ")

hour = datetime.now().hour

if 6 <= hour < 12:
    greeting = "Доброе утро"
elif 12 <= hour < 18:
    greeting = "Добрый день"
elif 18 <= hour < 24:
    greeting = "Добрый вечер"
else:
    greeting = "Доброй ночи"

print(f"{greeting}, {name}!")