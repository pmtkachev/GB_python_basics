# TASK 1
# def odd_nums(n):
#     for i in range(1, n + 1):
#         if i % 2 != 0:
#             yield i
#
#
# odd_to_15 = odd_nums(15)
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))


# TASK 2
odd_to_15 = (i for i in range(1, 16) if i % 2 != 0)
try:
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
except StopIteration:
    print('--StopIteration--')
