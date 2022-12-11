# TASK 4
import os

files_dict = {100: 0,
              1000: 0,
              10000: 0,
              100000: 0,
              1000000: 0}
sizes = [100, 1000, 10000, 100000, 1000000]

for root, dirs, files in os.walk('some_data'):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        for size in sizes:
            if file_size < size:
                files_dict[size] += 1
                break

print(files_dict)
