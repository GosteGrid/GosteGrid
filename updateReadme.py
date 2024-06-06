import os

# Путь к папке с гифками
gif_folder = "gif"

# Список гифок в нужном порядке
gif_list = [
    "test.gif",
    "test2.gif", 
    "test3.gif"
]

# Путь к файлу README
readme_file_path = "README.md"

# Чтение текущей гифки из файла README
with open(readme_file_path, "r") as readme_file:
    readme_content = readme_file.read()
    current_gif_index = (gif_list.index(readme_content.split("](")[1].split("/")[1]) + 1) if gif_list[-1] not in readme_content else 0

# Выбор следующей гифки по порядку
next_index = current_gif_index % len(gif_list)
next_gif = gif_list[next_index]

# Формирование ссылки на гифку
gif_link = f"![Random GIF]({gif_folder}/{next_gif})"

# Обновление файла README
with open(readme_file_path, "w") as readme_file:
    readme_file.write(gif_link)
