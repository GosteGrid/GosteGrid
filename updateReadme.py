import os
import json
import requests
import matplotlib.pyplot as plt

# Путь к папке с гифками
gif_dir = 'gif'

# Список файлов с гифками (можно также получить этот список динамически)
gifs = [
    "test.gif",
    "test2.gif",
    "test3.gif"
]

# Проверка существования директории с гифками
if not os.path.exists(gif_dir):
    print(f"Ошибка: Директория {gif_dir} не существует.")
    exit(1)

# Проверка наличия гифок
missing_gifs = [gif for gif in gifs if not os.path.isfile(os.path.join(gif_dir, gif))]
if missing_gifs:
    print(f"Ошибка: Следующие гифки отсутствуют в директории {gif_dir}: {missing_gifs}")
    exit(1)

# Чтение индекса последней использованной гифки
index_file = 'last_gif_index.json'
if os.path.exists(index_file):
    with open(index_file, 'r') as file:
        data = json.load(file)
        last_index = data.get('index', -1)
else:
    last_index = -1

# Выбор следующей гифки по кругу
next_gif_index = (last_index + 1) % len(gifs)
next_gif = gifs[next_gif_index]

# Формирование содержимого README.md с новой гифкой
readme_content = f"""
<a href="javascript:void(0)"> ![Гифка](video_2024-06-08_23-36-04.gif) </a>
<div align="center">

I'm a 1st year student pursuing a Bachelor's degree in Software Engineering at the Polytechnic University 👨‍🎓. I enjoy working with different technologies and exploring various fields, as well as learning new things 👾. Currently, I'm developing simple programs and implementing various data structures, which helps me understand their inner workings and principles of operation 💻.

</div>

<div align="center">
    <h2><img src="./pedro.gif" alt="Pedro" width="28"> Technology Stack <img src="./pedro.gif" alt="Pedro" width="28"> </h2> 
    <img src="./maket1.png" alt="C++" width="100">
    <img src="./maket2.png" alt="Python" width="100">
    <img src="./maket3.png" alt="Git" width="100">
</div>

<a href="javascript:void(0)"> <br> ![Гифка](gif/{next_gif}) </a>

<div align="center">
    <h2><img src="./redMan.gif" alt="Redman" width="32"> My GitHub Stats <img src="./redMan.gif" alt="Redman" width="32"></h2>

    

    # Введите ваше имя пользователя GitHub
    username = 'GosteGrid'

    # Получение данных о репозиториях
    repos_url = f'https://api.github.com/users/{username}/repos'
    repos_data = requests.get(repos_url).json()

    # Подсчет количества звезд
    stars = sum([repo['stargazers_count'] for repo in repos_data])

    # Для подсчета коммитов, PR и проблем потребуется дополнительный запрос к API для каждого репозитория
    commits = 0
    prs = 0
    issues = 0

    for repo in repos_data:
    # Получение данных о коммитах
    commits_url = f"https://api.github.com/repos/{username}/{repo['name']}/commits"
    commits_data = requests.get(commits_url).json()
    commits += len(commits_data)
    
    # Получение данных о PR
    prs_url = f"https://api.github.com/repos/{username}/{repo['name']}/pulls?state=all"
    prs_data = requests.get(prs_url).json()
    prs += len(prs_data)
    
    # Получение данных о проблемах
    issues_url = f"https://api.github.com/repos/{username}/{repo['name']}/issues?state=all"
    issues_data = requests.get(issues_url).json()
    issues += len(issues_data)

    # Пример простого графика
    labels = ['Stars', 'Commits', 'PRs', 'Issues']
    sizes = [stars, commits, prs, issues]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')  # Равные оси для кругового графика

    plt.savefig('maket1.png')
</div>

"""

# Запись содержимого в README.md
try:
    with open('README.md', 'w') as file:
        file.write(readme_content)
    print("README.md updated successfully")
except IOError as e:
    print(f"Ошибка при записи в README.md: {e}")
    exit(1)

# Обновление индекса последней использованной гифки
try:
    with open(index_file, 'w') as file:
        json.dump({'index': next_gif_index}, file)
    print(f"Индекс последней использованной гифки обновлен: {next_gif_index}")
except IOError as e:
    print(f"Ошибка при записи в {index_file}: {e}")
    exit(1)
