# TASK 3
import json
import sys

dict_users_hobby = {}
with open('users.csv', 'r', encoding='UTF-8') as users:
    with open('hobby.csv', 'r', encoding='UTF-8') as hobby:
        hobby_list = hobby.read().split('\n')
        users_list = users.read().split('\n')
        if len(users_list) < len(hobby_list):
            sys.exit(1)
        for i in range(len(users_list)):
            try:
                dict_users_hobby[users_list[i]] = hobby_list[i]
            except IndexError:
                dict_users_hobby[users_list[i]] = None

with open('dict_usr_hob.json', 'w', encoding='UTF-8') as file:
    dict_users_hobby = json.dumps(dict_users_hobby, ensure_ascii=False)
    file.write(dict_users_hobby)

# TASK 4
with open('users_hobby.txt', 'w', encoding='UTF-8') as users_hobby:
    with open('users.csv', 'r', encoding='UTF-8') as users:
        with open('hobby.csv', 'r', encoding='UTF-8') as hobby:
            hobby_list = hobby.read().split('\n')
            users_list = users.read().split('\n')
            for i in range(len(users_list)):
                try:
                    users_hobby.write(f'{users_list[i]}: {hobby_list[i]}\n')
                except IndexError:
                    users_hobby.write(f'{users_list[i]}: {None}\n')
