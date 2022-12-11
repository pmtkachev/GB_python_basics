# TASK 3
import os
import shutil

root_dir = 'project_folder\\'
templates = os.path.join(root_dir, 'templates\\')
try:
    os.makedirs(templates)
except FileExistsError:
    print(f'Папка {templates} уже существует!')

for root, dirs, files in os.walk(root_dir):
    if root.split('\\')[-1] == 'templates':
        for folder in dirs:
            shutil.copytree(os.path.join(root, folder), os.path.join(templates, folder), dirs_exist_ok=True)
