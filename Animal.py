class Animal:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    def move(self):
        pass

    @property
    def weight(self):
        return self.__weight

    @weight.getter
    def weight(self):
        return self.__weight

    # def get_weight(self):
    #     return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight <= 0:
            raise ValueError("Error, the weight has to be positive")
        else:
            self.__weight = new_weight

    @property
    def height(self):
        return self.__height

    @height.getter
    def height(self):
        return self.__height

    # def get_height(self):
    #     return self.__height

    @height.setter
    def height(self, new_height):
        if new_height <=0:
            raise ValueError("Error, the height has to be positive")
        else:
            self.__height = new_height


    def __str__(self):
        return "Taille de l'animal: " + str(self.height) + " Poids de l'animal: " + str(self.weight)

