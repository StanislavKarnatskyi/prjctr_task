def create_list() -> list:
    list_cat = []
    for i in range(1, 101):
        list_cat.append([f'cat{i}', 'without hat'])
    return list_cat


cats_with_hats_list = create_list()
cats_with_hats = []
edge = len(cats_with_hats_list)
count = 1
print(cats_with_hats_list)

while count <= edge:
    for i in range(1, len(cats_with_hats_list) + 1):
        if (i % count) == 0:
            if cats_with_hats_list[i - 1][1] == 'without hat':
                cats_with_hats_list[i - 1][1] = 'with hat'
            else:
                cats_with_hats_list[i - 1][1] = 'without hat'
    count += 1

for i in range(len(cats_with_hats_list)):
    if cats_with_hats_list[i][1] == 'with hat':
        cats_with_hats.append(cats_with_hats_list[i])

print(cats_with_hats)
