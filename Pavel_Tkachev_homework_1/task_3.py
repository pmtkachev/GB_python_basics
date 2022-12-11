# Task 3
percents = [i for i in range(1, 101)]

for num in percents:
    if num % 10 == 1 and num // 10 != 1:
        print(f'{num} процент')
    elif (num % 10 == 2 or num % 10 == 3 or num % 10 == 4) and num // 10 != 1:
        print(f'{num} процента')
    else:
        print(f'{num} процентов')
