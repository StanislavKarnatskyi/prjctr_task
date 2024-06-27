import csv

list_ = []

with open('../lecture_10_task_3/game_result/result.csv', 'r') as file:
    text = csv.reader(file)
    next(text)
    for row in text:
        list_.append(row)
print(list_)