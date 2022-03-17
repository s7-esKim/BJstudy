word = input().upper()

word_dict = {}
for i in word:
    if i in word_dict.keys():
        word_dict[i] += 1
    else:
        word_dict[i] = 1

max_value =0

for key, value in word_dict.items():
    if value > max_value:
        max_value = value
        max_key = [key]
    elif value == max_value:
        max_key.append(key)

if len(max_key)>1:
    print('?')
else:
    print(max_key[0])