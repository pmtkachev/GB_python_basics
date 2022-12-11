# TASK 5
import sys

# В первом параметре задаем исходное имя файла с пользователями
# Во втором параметре задаем исходное имя файла с хобби
# В третьем параметре задаем имя выходного файла

try:
    with open(sys.argv[3], 'w', encoding='UTF-8') as users_hobby:
        with open(sys.argv[1], 'r', encoding='UTF-8') as users:
            with open(sys.argv[2], 'r', encoding='UTF-8') as hobby:
                hobby_list = hobby.read().split('\n')
                users_list = users.read().split('\n')
                for i in range(len(users_list)):
                    try:
                        users_hobby.write(f'{users_list[i]}: {hobby_list[i]}\n')
                    except IndexError:
                        users_hobby.write(f'{users_list[i]}: {None}\n')
except IndexError:
    print('Необходимо ввести параметры скрипта:')
    print('В первом параметре задаем исходное имя файла с пользователями\n'
          'Во втором параметре задаем исходное имя файла с хобби\n'
          'В третьем параметре задаем имя выходного файла')
