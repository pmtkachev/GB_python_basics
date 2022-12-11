# TASK 1
import re


def email_parse(email):
    pattern = re.compile(r'(?P<username>\w+)[@](?P<domain>\w+\.\w+)')
    result = re.match(pattern, email)
    if result:
        result = result.groupdict()
        return result
    else:
        raise ValueError(f'wrong email: {email}')


print(email_parse('someone@geekbrains.ru'))
print(email_parse('ptka4ev@mail.ru'))
print(email_parse('someone@geekbrainsru'))

