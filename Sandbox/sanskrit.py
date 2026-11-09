import json
with open("C:/Users/Manish/Desktop/sanskrit.txt", "r",  encoding='utf-8') as file:
    text = file.read()

text_list = text.split(" ")
hash_map = {}
for text in text_list:
    if text in hash_map:
        hash_map[text] += 1
    else:
        hash_map[text] = 1

with open("C:/Users/Manish/Desktop/kk.txt", "w", encoding="utf-8") as file:
    json_map = json.dumps(hash_map,  ensure_ascii=False)
    file.write(json_map)

print(len(set(text_list)))