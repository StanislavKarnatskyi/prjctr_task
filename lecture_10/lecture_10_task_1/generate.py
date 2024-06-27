from random import randint

summary = open('summary.txt', 'w+')

for i in range(26):
    with open('a-z/' + chr(65 + i) + '.txt', 'w') as file:
        file.write(f'{randint(1, 100)}')

for i in range(26):
    with open('a-z/' + chr(65 + i) + '.txt', 'r') as file:
        text = file.read()
        summary.write(f'{chr(65 + i)}.txt: {text}\n')

summary.close()

