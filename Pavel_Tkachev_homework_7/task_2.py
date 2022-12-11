# TASK 2
import os
import json

main_dir = 'project_folder'

with open('config.yaml', 'r', encoding='UTF-8') as config:
    config = json.loads(config.read())

try:
    os.mkdir(main_dir)
    for key, value in config.items():
        os.makedirs(os.path.join(main_dir, key))
        for file in value:
            with open(os.path.join(main_dir, key, file), 'w', encoding='UTF-8') as f:
                pass
except FileExistsError:
    print(f'Файл или папка уже существует!')

