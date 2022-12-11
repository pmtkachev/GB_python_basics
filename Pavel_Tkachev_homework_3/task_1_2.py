trans_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(translate_dict, number_str):
    value = translate_dict.get(number_str.lower())
    if number_str[0].istitle():
        try:
            value = value.title()
        except AttributeError:
            pass
    return value


print(num_translate_adv(trans_dict, 'one'))
print(num_translate_adv(trans_dict, 'two'))
print(num_translate_adv(trans_dict, 'Eight'))
print(num_translate_adv(trans_dict, 'Ten'))
print(num_translate_adv(trans_dict, 'Hello'))
print(num_translate_adv(trans_dict, 'hello'))
