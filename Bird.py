from Animal import Animal


class Bird(Animal):
    def __init__(self, weight, height,max_flying_altitude):
        super().__init__(weight, height, )
        self.max_flying_altitude = max_flying_altitude

    def move(self):
        return "I fly"

