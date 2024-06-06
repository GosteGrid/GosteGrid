import os

# Путь к папке с гифками
gif_folder = "gif"

# Список гифок в нужном порядке
gif_list = [
    "test.gif",
    "test2.gif"
]

# Название последней использованной гифки
last_gif = "test2.gif"

# Поиск индекса последней использованной гифки в списке
last_index = gif_list.index(last_gif)

# Выбор следующей гифки по порядку
next_index = (last_index + 1) % len(gif_list)
next_gif = gif_list[next_index]

# Формирование ссылки на гифку
gif_link = f"![Random GIF]({gif_folder}/{next_gif})"

# Обновление файла README
with open("README.md", "r+") as readme_file:
    lines = readme_file.readlines()
    for i, line in enumerate(lines):
        if "![Random GIF]" in line:
            lines[i] = gif_link + "\n"
            break
    else:
        lines.append("\n" + gif_link + "\n")
    readme_file.seek(0)
    readme_file.writelines(lines)
    readme_file.truncate()
