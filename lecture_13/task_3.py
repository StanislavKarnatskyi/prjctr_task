class Car:
    def __init__(self, name: str, model: str, year: int, speed: int):
        self.name = name
        self.model = model
        self.year = year
        if speed < 0:
            raise ValueError("Speed must be greater than 0")
        else:
            self.speed = speed

    def accelerate(self):
        self.speed += 5
        return self.speed

    def brake(self):
        self.speed -= 5
        if self.speed >= 0:
            return self.speed
        else:
            raise ValueError("Speed can't be below 0")

    def display_speed(self):
        return self.speed


