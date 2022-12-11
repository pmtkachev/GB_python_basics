def thesaurus(*args):
    dict_names = {}
    for name in args:
        if name[0] in dict_names.keys():
            list_names = dict_names.get(name[0])
            list_names.append(name)
            dict_names[name[0]] = list_names
            continue
        dict_names[name[0]] = [name]
    return dict_names


dict_result = thesaurus("Иван", "Мария", "Петр", "Илья", "Анастасия")
print(dict_result)
dict_result = dict(sorted(dict_result.items(), key=lambda x: x[0]))
print(dict_result)

# 4 задачку решил не делать, со *.
