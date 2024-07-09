class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other):
        """
            Task 1
            "Add" without using magic method
        """
        return Country(self.name + ' ' + other.name, self.population + other.population)

    def __add__(self, other):
        """
            Task 2
            "Add" using magic method
        """
        return Country(self.name + ' ' + other.name, self.population + other.population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.name, bosnia_herzegovina.population)

bosnia_herzegovina = None
print(bosnia_herzegovina)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.name, bosnia_herzegovina.population)
