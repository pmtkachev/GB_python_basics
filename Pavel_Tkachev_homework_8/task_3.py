# TASK 3
# Для позиционных аргументов
# def type_logger(func):
#     def wrapper(*args):
#         result = ''
#         for _ in args:
#             result += f'{_}: {type(_)}, '
#         return result[0:-2]
#     return wrapper

# Для именованных аргументов
def type_logger(func):
    def wrapper(**kwargs):
        result = ''
        for k, v in kwargs.items():
            result += f'{v}: {type(v)}, '
        return result[0:-2]
    return wrapper


@type_logger
def calc_cube(x=1, y=1):
    return x ** y


a = calc_cube(x=5, y=3.0)
print(a)


