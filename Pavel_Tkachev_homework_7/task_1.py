# TASK 1
import os

main_dir = 'my_project'
project_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    for folder in project_dirs:
        os.makedirs(os.path.join(main_dir, folder))
else:
    print(f'Папка {main_dir} уже существует!')
