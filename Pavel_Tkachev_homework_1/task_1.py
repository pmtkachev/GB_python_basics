# Task 1
duration_list = [53, 153, 4153, 400153]

for duration in duration_list:
    if 0 <= duration < 60:
        print(f'{duration} сек')
    elif 60 <= duration < 3600:
        print(f'{duration // 60} мин {duration % 60} сек')
    elif 3600 <= duration < 86400:
        hours = duration // 3600
        minutes = (duration - hours * 3600) // 60
        secs = duration - (hours * 3600 + minutes * 60)
        print(f'{hours} час {minutes} мин {secs} сек')
    else:
        days = duration // 86400
        hours = (duration - (days * 86400)) // 3600
        minutes = (duration - hours * 3600 - days * 86400) // 60
        secs = duration - (hours * 3600 + minutes * 60 + days * 86400)
        print(f'{days} дн {hours} час {minutes} мин {secs} сек')
