class Robot:
    def __init__(self, orientation=None, position_x=0, position_y=0):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        match self.orientation:
            case 'up':
                self.position_y += steps
            case 'down':
                self.position_y -= steps
            case 'left':
                self.position_x -= steps
            case 'right':
                self.position_x += steps
            case _:
                raise ValueError(f"Unknown value --> {self.orientation}")

    def turn(self, direction):
        dict_direction = ['left', 'right', 'up', 'down']
        if direction.lower() in dict_direction:
            for side in dict_direction:
                if side == direction.lower():
                    self.orientation = direction.lower()
        else:
            raise ValueError("Unknown value")

    def display_position(self):
        print(f'Coordinates X: {self.position_x} Y: {self.position_y}\nOrientation: {self.orientation}')

