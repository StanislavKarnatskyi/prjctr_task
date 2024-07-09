import pytest
from task_1_and_task_2 import Country
from task_3 import Car
from task_4 import Robot


@pytest.mark.parametrize("first_country, second_country, first_population, second_population, expected_country, "
                         "expected_population", [
    ('Bosnia', 'Herzegovina', 10_000_000, 5_000_000, 'Bosnia Herzegovina', 15_000_000),
    ('Czechia', 'Slovakia', 5_000_000, 2_000_000, 'Czechia Slovakia', 7_000_000),
    ('Lithuania', 'Poland', 3_000_000, 40_000_000, 'Lithuania Poland', 43_000_000)
])
def test_add(first_country, second_country, first_population, second_population, expected_country, expected_population):
    """
    Task 1
    Create Class to merge to county to one
    Done using return keyword combined with operator addition
    function can be called by using .add()

    Examples:
        bosnia = Country('Bosnia', 10_000_000)
        herzegovina = Country('Herzegovina', 5_000_000)

        bosnia_herzegovina = bosnia.add(herzegovina)
    print(bosnia_herzegovina.name, bosnia_herzegovina.population)
    # Output: 'Bosnia Herzegovina' 15000000

    ----

    Test checking if in correct way addition going

    """
    country1 = Country(first_country, first_population)
    country2 = Country(second_country, second_population)
    country_add = country1.add(country2)
    assert country_add.name == expected_country
    assert country_add.population == expected_population

@pytest.mark.parametrize("first_country, second_country, first_population, second_population, expected_country, "
                         "expected_population", [
    ('Bosnia', 'Herzegovina', 10_000_000, 5_000_000, 'Bosnia Herzegovina', 15_000_000),
    ('Czechia', 'Slovakia', 5_000_000, 2_000_000, 'Czechia Slovakia', 7_000_000),
    ('Lithuania', 'Poland', 3_000_000, 40_000_000, 'Lithuania Poland', 43_000_000)
])
def test_add_magic(first_country, second_country, first_population, second_population, expected_country, expected_population):
    """
    Task 2
    Create Class to merge to county to one using magic method
    Done using return keyword combined with operator addition
    function can be called by using operator addition

    Examples:
        bosnia = Country('Bosnia', 10_000_000)
        herzegovina = Country('Herzegovina', 5_000_000)

        bosnia_herzegovina = bosnia + herzegovina
    print(bosnia_herzegovina.name, bosnia_herzegovina.population)
    # Output: 'Bosnia Herzegovina' 15000000
    ----

    Test checking if in correct way addition going
    """
    country1 = Country(first_country, first_population)
    country2 = Country(second_country, second_population)
    country_add = country1 + country2
    assert country_add.name == expected_country
    assert country_add.population == expected_population

@pytest.mark.parametrize("name, model, year, speed, expected_speed_break", [
    ("Toyota", "Camry", 2020, 50, 45),
    ("Honda", "Civic", 2019, 60, 55),
    ("Ford", "Mustang", 2021, 70, 65)
])
def test_car_break(name, model, year, speed, expected_speed_break):
    """
    Task 3
    Create Class Car with some attributes
    This test checking if car can be slower
    Calling .brake() car get slower on 5 km/hr
    """
    test_car = Car(name, model, year, speed)
    test_car.brake()
    assert test_car.speed == expected_speed_break

@pytest.mark.parametrize("name, model, year, speed, expected_speed_accelerate", [
    ("Toyota", "Camry", 2020, 50, 55),
    ("Honda", "Civic", 2019, 60, 65),
    ("Ford", "Mustang", 2021, 70, 75)
])
def test_car_accelerate(name, model, year, speed, expected_speed_accelerate):
    """
        Task 3
        Create Class Car with some attributes
        This test checking if car can gain speed
        Calling .brake() car get faster on 5 km/hr
    """
    test_car = Car(name, model, year, speed)
    test_car.accelerate()
    assert test_car.speed == expected_speed_accelerate

@pytest.mark.parametrize("name, model, year, speed, expected_speed", [
    ("Toyota", "Camry", 2020, 50, 50),
    ("Honda", "Civic", 2019, 60, 60),
    ("Ford", "Mustang", 2021, 70, 70)
])
def test_car_accelerate(name, model, year, speed, expected_speed):
    """
        Task 3
        Create Class Car with some attributes
        This test checking if car created with correct attribute, like speed
    """
    test_car = Car(name, model, year, speed)
    assert test_car.speed == expected_speed


def test_robot_exist():
    """
    Task 4
    Create Robot with default parameters
    orientation=None, position_x=0, position_y=0
    """
    boston = Robot()
    assert boston.orientation is None
    assert boston.position_x == 0
    assert boston.position_y == 0


@pytest.mark.parametrize("direction, turn_direction, expected_direction", [
    ('left', 'right', 'right'),
    ('left', 'up', 'up'),
    ('left', 'down', 'down'),
    ('right', 'down', 'down'),
    ('right', 'up', 'up'),
    ('right', 'left', 'left'),
    ('down', 'left', 'left'),
    ('down', 'right', 'right'),
    ('down', 'up', 'up'),
    ('up', 'down', 'down'),
    ('up', 'right', 'right'),
    ('up', 'left', 'left')
])
def test_change_direction(direction, turn_direction, expected_direction):
    """
    Task 4
    Checking if robot turn in the right direction
    Function can be called by .turn(<side_to_turn>)
    """
    boston = Robot(orientation=direction)
    boston.turn(turn_direction)
    assert boston.orientation == expected_direction

@pytest.mark.parametrize("direction, step, expected_x, expected_y",[
    ('left', 4, -4, 0),
    ('right', 8, 8, 0),
    ('down', 2, 0, -2),
    ('up', 3, 0, 3)
])
def test_step(direction, step, expected_x, expected_y):
    """
    Task 4
    Checking if robot can change direction x y
    Function can be called by .move(<number_of_steps>)
    """
    boston = Robot()
    boston.turn(direction)
    boston.move(step)
    assert boston.position_x == expected_x
    assert boston.position_y == expected_y
