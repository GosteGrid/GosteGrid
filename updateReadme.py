import random

# Список гифок
gif_list = [
    "gif/test.gif",
    "test2.gif"
]

# Выбор случайной гифки
random_gif = random.choice(gif_list)

# Формирование ссылки на гифку
gif_link = f"![Random GIF]({random_gif})"

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
