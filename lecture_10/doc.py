import pytest
import csv
from lecture_10_task_1.generate import create_list_a_to_z
from lecture_10_task_2.change_case import from_lower_to_upper
from lecture_10_task_3.simulate import simulate_game
from lecture_10_task_3.simulate import create_csv
from lecture_10_task_4.highest_score import generate_csv_with_highest_score

"""
    Lecture 10. Task 1. Create_list_a_to_z 
    In this task need to create list of txt files from a to z, and each one contain random number.
    After need to read each of one files and write their name and random number into summary
    
    To complete was used:
        - built-in library 'random', more precisely randint(1, 100) to generate random number
        - context manager (with) for each operation, like reading and writing
    
    Note:
        - need to create folder 'a-z' to contain all files which was created
        
        Lecture 10. Task 2. From .txt file with some text convert to .txt with uppercase
    In this task need to access to text with some lowercase read and save. After create file where uppercase text 
    will be placed. Take from save text with lowercase and write it to uppercase.txt using build-in function .upper()
    
    To complete was used:
        - context manager (with) for each operation, like reading and writing
        - built-in function .upper()  
        
        
        Lecture 10. Task 3. Create list of 5 people which play game. Write they result into .csv file
    
    In this task need to create simulation of game, where each player play 100 rounds. 
    Their results write to .csv file
    
    To complete was used:
        - built-in library csv 
        - context manager(with) to create and write 
        - built-in library random, to create score of user
        
        Lecture 10. Task 4. From previous task use .csv file for sorting and writing highest score 
        
    In this task need to open .csv file to read it and after write it to another .csv but sorted. 
    Must be two files, one with top 5 scores, another with sorted players with their scores from top to bottom     
    (on top player with highest score, on bottom with lowest)
    
    To complete was used:
         - built-in library csv 
         - context manager(with) to create and write 
         -built-in function to sort items
"""


@pytest.mark.parametrize('param_char', 'abcdefghijklmnopqrstuvwxyz')
def test_check_range(param_char):
    """
        Test to check if number inside file in range

        Should be checked numbers inside of file, must be in range from 1 to 100
    """
    with open(f'lecture_10_task_1/a-z/{param_char}.txt', 'r') as file:
        text = int(file.read())
        if 1 < text < 101:
            pass
        else:
            raise ValueError


@pytest.mark.parametrize('param_char', 'abcdefghijklmnopqrstuvwxyz')
def test_check_exist(param_char):
    """
        Test to check if file exist and can be open
    """
    try:
        with open(f'lecture_10_task_1/a-z/{param_char}.txt', 'r') as file:
            text = file.read()
    except:
        raise ValueError


def test_identity():
    """
     Test to check if lower case text and upper case text are similar

    """
    with open('lecture_10_task_2/lowercase_text.txt', 'r') as file_lower, open('lecture_10_task_2/uppercase_text.txt',
                                                                               'r') as file_upper:
        text_lower = file_lower.read()
        text_upper = file_upper.read()
        if text_lower.lower() == text_upper.lower():
            pass
        else:
            raise ValueError


@pytest.mark.parametrize('param', [
    'lecture_10_task_2/lowercase_text.txt',
    'lecture_10_task_2/uppercase_text.txt'
])
def test_check_length(param):
    """
        Test to check files length, purpose for it that file shouldn't be empty

    """
    with open(param, 'r') as file:
        text = file.read()
        text_len = len(text)
        if text_len > 0:
            pass
        else:
            raise ValueError


@pytest.mark.parametrize('param4', ['uppercase_text.txt'])
def test_from_lower_to_upper_check_length(param4):
    """
        Test to check if uppercase_text.txt is in upper case or not
    """
    with open(f'lecture_10_task_2/{param4}', 'r') as file:
        text = file.read()
        if text.isupper():
            pass
        else:
            raise ValueError


def test_simulate_game():
    """
        Test to check if function number in range
    """
    result_1 = simulate_game()
    assert 0 < result_1 < 1001, 'ValueError: Out of range'
    result_2 = simulate_game()
    assert 0 < result_2 < 1001, 'ValueError: Out of range'
    result_3 = simulate_game()
    assert 0 < result_3 < 1001, 'ValueError: Out of range'

def test_check_title():
    """
        Test to check correct title or not
    """
    with open('lecture_10_task_3/game_result/result.csv', 'r') as csv_file:
        text = csv.reader(csv_file)
        text_title = next(text)
        if text_title == ['Player name', 'Score']:
            pass
        else:
            raise ValueError


def test_numbers_of_games():
    """
        Test to check if in correct way was created csv file with player name and score.
        Checking if right amount of games was created
    """
    list_ = []
    dict_ = {}
    with open('lecture_10_task_3/game_result/result.csv', 'r') as file:
        text = csv.DictReader(file)
        for row in text:
            list_.append(row)
    for i in range(len(list_)):
        if list_[i]['Player name'] in dict_.keys():
            dict_[list_[i]['Player name']] = dict_[list_[i]['Player name']] + 1
        else:
            dict_.update({list_[i]['Player name']: 1})
    if (len(dict_) * 100) == sum(dict_.values()):
        pass
    else:
        raise ValueError


def test_score():
    """
        Test to check if in csv all files in range from 1 to 1000
    """
    list_ = []
    with open('lecture_10_task_3/game_result/result.csv', 'r') as file:
        text = csv.DictReader(file)
        for row in text:
            list_.append(row)
    for i in range(len(list_)):
        if 0 < int(list_[i]['Score']) < 1001:
            pass
        else:
            raise ValueError