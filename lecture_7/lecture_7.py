import random


# Task 1
def random_county_capital():
    capitals = {
        'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
        'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa',
        'Switzerland': 'Bern', 'Austria': 'Vienna',
        'Belgium': 'Brussels', 'Sweden': 'Stockholm',
        'Norway': 'Oslo', 'Denmark': 'Copenhagen',
        'Finland': 'Helsinki', 'Poland': 'Warsaw',
        'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'
    }
    return random.choice(list(capitals.items()))


def guess_capital():
    country, capital = random_county_capital()
    user_guess = input(f'Guess the capital of {country}.\nEnter: ')
    score, life, count, hint = 0, 3, 0, ''
    while True:
        if user_guess.lower() == capital.lower():
            score += 1
            count = 0
            hint = ''
            print(f"You're right! Your score is now {score}")
            country, capital = random_county_capital()
            user_guess = input(f'Guess the capital of {country}.\nEnter: ')
        elif user_guess.lower() == 'exit':
            print(f'Game over! Your final score is {score}.')
            break
        else:
            life -= 1
            if life < 0:
                print(f'Game over! You lost all of your life. Final score is {score}.')
                break
            print(f'Incorrect. You lost one life. Lives remaining: {life}.')
            hint += capital[count]
            user_guess = input(f'There\'s hint {hint}. Try again: ')
            count += 1


# Task 2

# def roman_to_int(s: str) -> int:
#     roman = {
#         1000: 'M',
#         900: 'CM',
#         500: 'D',
#         400: 'CD',
#         100: 'C',
#         90: 'XC',
#         50: 'L',
#         40: 'XL',
#         10: 'X',
#         9: 'IX',
#         5: 'V',
#         4: 'IV',
#         1: 'I'}
#
#     num = 1998
#     string = ''
#
#     roman_keys = roman.keys()
#     for keys in roman_keys:
#         if (num - keys) >= 0:
#             num = num - keys
#             string += roman[keys]
#
#     print(string)
#
#
# roman_to_int('fd')
#
#
# def test_roman_to_int():
#     result1 = roman_to_int("III")
#     assert result1 == 3
#     result1 = roman_to_int("LVIII")
#     assert result1 == 58
#     result1 = roman_to_int("MCMXCIV")
#     assert result1 == 1994


# Task 4
def majority_element(nums: list) -> int:
    nums_to_set = (list(set(nums)))
    count = []
    for i in nums_to_set:
        count.append(nums.count(i))
    for i in range(len(count)):
        if count[i] == max(count):
            return nums_to_set[i]


majority_element([3, 2, 3])
majority_element([2, 2, 1, 1, 1, 2, 2])


def test_majority_element():
    result1 = majority_element([3, 2, 3])
    assert result1 == 3
    print('Task 4\nResult 1 completed')
    result2 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result2 == 2
    print('Task 4\nResult 2 completed')


# Task 5
def get_subjects_not_passed_by_all_students(exams):
    bad_result = []
    bad_subjects = []
    good_result = []
    for i in range(len(exams)):
        if exams[i][1] < 60:
            bad_result.append(exams[i])
        else:
            good_result.append(exams[i])

    for i in range(len(bad_result)):
        if i in good_result:
            bad_result.pop(i)

    for i in range(len(bad_result)):
        bad_subjects.append(bad_result[i][2])

    bad_subjects = set(bad_subjects)
    return bad_subjects


def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 55, "Math"),
        ("Bob", 40, "Math"),
        ("Charlie", 30, "Math"),
        ("Alice", 50, "Science"),
        ("Bob", 45, "Science"),
        ("Charlie", 40, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]

    assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}
    print('Task 5\nCompleted')


print('1. Write a game where the user should guess the capital of the country that you have in your dictionary.')
print('4. Given a list of integers of size n, return the majority element.')
print('5. Find missing subjects.')

while True:
    choose_task = 'exit' #input("Choose task 1 - 5: ")
    if choose_task == 'exit':
        print('Bye')
        break
    elif choose_task == '1':
        guess_capital()
    elif choose_task == '2':
        pass
    elif choose_task == '3':
        pass
    elif choose_task == '4':
        test_majority_element()
    elif choose_task == '5':
        test_get_subjects_not_passed_by_all_students()
    else:
        print("Enter only valid numbers")
