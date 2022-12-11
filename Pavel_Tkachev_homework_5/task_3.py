# TASK 3
def gen_tutors(tutors, klasses):
    for i in range(len(tutors)):
        if i > len(klasses) - 1:
            yield tutors[i], None
        else:
            yield tutors[i], klasses[i]


teachers = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Павел'
]

classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

result = gen_tutors(teachers, classes)
print(result)  # Генератор
try:
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
except StopIteration:
    print('StopIteration')
