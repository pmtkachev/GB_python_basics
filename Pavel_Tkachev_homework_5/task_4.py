# TASK 4
def numbers(number_list):
    num = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] > num:
            yield number_list[i]
        num = number_list[i]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = list(numbers(src))
print(result)
