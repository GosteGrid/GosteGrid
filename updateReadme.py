import random

# Получение списка видео файлов
gifs = [
    "gif/test.gif", 
    "0420-ezgif.com-video-to-gif-converter.gif"
]

# Выбор случайного видео
chosen_gif = random.choice(gifs)

# Создание содержимого README.md
readme_content = f"""
# Привет!

Добро пожаловать в мой профиль! Вот случайное видео для вас:

![Видео]({chosen_gif})
"""

# Запись содержимого в README.md
with open('README.md', 'w') as file:
    file.write(readme_content)
