# Task 2
def sum_numbers(numbers):
    result_sum = 0
    for number in numbers:
        num = number
        result = 0
        while num > 0:
            result += num % 10
            num = num // 10
        if result % 7 == 0:
            result_sum += number
    return result_sum


numbers_list = [i ** 3 for i in range(1000) if not i % 2 == 0]

print(sum_numbers(numbers_list))

for i in range(len(numbers_list)):
    numbers_list[i] += 17

print(sum_numbers(numbers_list))
