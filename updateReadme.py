import random

# Получение списка видео файлов
gifs = [
    "gif/first.gif",
    "gif/second.gif"
]

# Выбор случайного видео
chosen_gif = random.choice(gifs)

# Формирование URL видео для отображения в README
gifs_url = f'https://raw.githubusercontent.com/GosteGrid/GosteGride/main/gif/{chosen_gif}'

# Создание содержимого README.md
readme_content = f"""
# Привет!

Добро пожаловать в мой профиль! Вот случайное видео для вас:

![Видео]({gifs_url})
"""

# Запись содержимого в README.md
with open('README.md', 'w') as file:
    file.write(readme_content)
