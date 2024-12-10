import os
import sys

dir = sys.argv[1]
files = []
for name in os.listdir(dir):
    path = os.path.join(dir, name)
    files.append(path)

dict_files = {}
for i in files:
    dict_files[i] = os.path.getsize(i)

sorted_dict = {}
sorted_keys = sorted(dict_files.items(), key=lambda x: x[1], reverse=True)
print(sorted_keys[0])

for i in range(0, len(sorted_keys) - 1):
    print(str(sorted_keys[i]).replace("(", "").replace(")", "").replace(",", ":"))
