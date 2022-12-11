# TASK 1
import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
result = [(i.split(' -')[0], i.split(' "')[1].split()[0], i.split(' "')[1].split()[1]) for i in
          response.text.split('\n')[0:-1]]


# TASK 2
dict_spam = {}
for j in result:
    if j[0] in dict_spam:
        dict_spam[j[0]] += 1
        continue
    dict_spam[j[0]] = 1

ip = list(dict_spam.keys())[list(dict_spam.values()).index(max(dict_spam.values()))]
print(f'Больше всего запросов с ip: {ip}\nКоличество: {max(dict_spam.values())}')
