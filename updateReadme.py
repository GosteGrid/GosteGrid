import os
import random

last_gif_file = 'last_gif_file.txt'

# Получение списка видео файлов
gifs = [
    "gif/test.gif", 
    "gif/test2.gif"
]

if os.path.exists(last_gif_file):
    with open(last_gif_file, 'r') as file:
        last_gif = file.read().strip()
else:
    last_gif = None

# Выбор новой гифки, отличной от предыдущей
chosen_gif = random.choice(gifs)
while chosen_gif == last_gif and len(gifs) > 1:
    chosen_gif = random.choice(gifs)

with open(last_gif_file, 'w') as file:
    file.write(chosen_gif)
# Создание содержимого README.md
readme_content = f"""
# Привет!

Добро пожаловать в мой профиль! Вот случайное видео для вас:

![Видео]({chosen_gif})
"""

# Запись содержимого в README.md
with open('README.md', 'w') as file:
    file.write(readme_content)
