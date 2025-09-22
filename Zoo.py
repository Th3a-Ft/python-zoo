from operator import concat

from Animal import Animal

class Zoo:
    list_animal = []

    def __init__(self, list_animal):
       self.list_animal = list_animal

    def add_animal(self, animal):
        self.list_animal.append(animal)
        return self.list_animal

    def get_list_animal(self):
        return self.list_animal

    def __add__(self, zoo1,zoo2):
        zoo1 = zoo1.get_list_animal()
        zoo2 = zoo2.get_list_animal()
        zoo3 = zoo1 + zoo2
        return zoo3










