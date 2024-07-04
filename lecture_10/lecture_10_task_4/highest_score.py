import csv

def generate_csv_with_highest_score(file_path: str):
    list_ = []
    highest_list = []

    with open(file_path, 'r') as file:
        text = csv.reader(file)
        next(text)
        for row in text:
            list_.append(row)
    list_sorted = sorted(list_, key=lambda x: int(x[1]), reverse=True)
    with open('highest_score/sorted_score.csv', 'w') as file:
        text = csv.writer(file)
        for i in range(len(list_sorted)):
            text.writerow(list_sorted[i])
    with open('highest_score/sorted_score.csv', 'r') as file:
        with open('highest_score/highest_score.csv', 'w') as file1:
            text = csv.reader(file)
            text1 = csv.writer(file1)
            for row in text:
                highest_list.append(row)
            for i in range(5):
                text1.writerow(highest_list[i])


