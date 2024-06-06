import random

# Получение списка видео файлов
videos = [
    "video/pinterestdownloader.com-1717659520.295921.mp4",
    "video/pinterestdownloader.com-1717659547.902296.mp4",
    "video/pinterestdownloader.com-1717659575.377558.mp4"
]

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
