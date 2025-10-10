from datetime import datetime

# ввод имени
name = input("Введите ваше имя: ")

# получение текущего часа
hour = datetime.now().hour

# определяем приветствие
if 6 <= hour < 12:
    greeting = "Доброе утро"
elif 12 <= hour < 18:
    greeting = "Добрый день"
elif 18 <= hour < 24:
    greeting = "Добрый вечер"
else:
    greeting = "Доброй ночи"

# вывод результата
print(f"{greeting}, {name}!")