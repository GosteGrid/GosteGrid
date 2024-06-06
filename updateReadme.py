import os
import random

# Путь к папке с видео
videos_dir = 'video'

# Получение списка видео файлов
videos = [f for f in os.listdir(videos_dir) if os.path.isfile(os.path.join(videos_dir, f))]

# Выбор случайного видео
chosen_video = random.choice(videos)

# Формирование URL видео для отображения в README
video_url = f'https://raw.githubusercontent.com/GosteGrid/GosteGride/main/video/{chosen_video}'

# Создание содержимого README.md
readme_content = f"""
# Привет!

Добро пожаловать в мой профиль! Вот случайное видео для вас:

![Видео]({video_url})
"""

# Запись содержимого в README.md
with open('README.md', 'w') as file:
    file.write(readme_content)
