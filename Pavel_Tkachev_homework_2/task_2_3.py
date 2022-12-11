# Думаю эту задачу можно было бы решить проще и лаконичнее, но я додумался только так =)

string_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for value in string_list[:]:
    if value.isdigit():
        string_list.insert(string_list.index(value), '"')
        string_list.insert(string_list.index(value) + 1, '"')
        string_list[string_list.index(value)] = f'{int(value):02}'
    elif value[1:].isdigit():
        string_list.insert(string_list.index(value), '"')
        string_list.insert(string_list.index(value) + 1, '"')
        string_list[string_list.index(value)] = f'{value[0]}{int(value[1:]):02}'

result_string = ' '.join(string_list)
count = 0

for i in result_string:
    if i == '"' and count % 2 == 0:
        result_string = result_string.replace(' " ', ' "', 1)
        count += 1
        continue
    elif i == '"':
        count += 1
        result_string = result_string.replace(' " ', '" ', 1)

print(result_string)
