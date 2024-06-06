import os
import random

# Путь к папке с гифками
gif_dir = 'gif'

# Получение списка файлов с расширением .gif
gifs = [
    "test.gif",
    "test2.gif",
    "test3.gif"
]

# Выбор случайной гифки
chosen_gif = random.choice(gifs)

# Получение индекса выбранной гифки
gif_index = gifs.index(chosen_gif)

# Получение следующей гифки (с учетом цикличности)
next_gif_index = (gif_index + 1) % len(gifs)
next_gif = gifs[next_gif_index]

# Формирование содержимого README.md с новой гифкой
readme_content = f"""
# Привет!

Добро пожаловать в мой профиль! Вот случайная гифка для вас:

![Гифка](gifs/{next_gif})
"""

# Запись содержимого в README.md
with open('README.md', 'w') as file:
    file.write(readme_content)
