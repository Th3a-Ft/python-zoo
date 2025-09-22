import pytest

from Animal import Animal
from Bird import Bird
from Serpent import Snake
from Zoo import Zoo


def test_class_animal():
    animal = Animal(24, 87)
    # Condition yoda pour les getters
    # Les getters == / les setters 1
    assert 24 == animal.weight
    assert 87 == animal.height


def test_move_snake():
    serpent = Snake(12, 84)
    assert "I crawl" == serpent.move()


def test_move_bird():
    bird = Bird(24, 65, 1500)
    assert "I fly" == bird.move()


def test_validate_data():
    bird = Bird(45, 12, 400)
    # assert bird.set_weight(-12) == "Error, the weight has to be positive"
    bird.weight = 25
    # assert bird.weight == 25
    assert 25 == bird.weight
    # assert bird.set_height(-89) == "Error, the weight has to be positive"
    bird.height = 84
    assert bird.height == 84

    with pytest.raises(ValueError):
        snake = Snake(87, 45)
        snake.height = -12
        assert "Error, the weight has to be positive" == snake.height

    with pytest.raises(ValueError):
        bird = Bird(87, 45, 600)
        bird.weight = -12
        assert "Error, the height has to be positive" == bird.height


def test_list():
    snake = Snake(25, 10)
    bird = Bird(45, 87, 1500)
    zoo = Zoo([snake, bird])
    assert zoo.list_animal == [snake, bird]
    donkey = Animal(45, 32)
    assert zoo.add_animal(donkey) == [snake, bird, donkey]


def test_tostring():
    ani = Animal(47, 96)
    assert ani.__str__() == "Taille de l'animal: 96 Poids de l'animal: 47"


def test_add_zoo():
    donkey = Animal(80, 95)
    tiger = Animal(96, 52)
    giraffe = Animal(87, 256)
    mouse = Animal(2, 35)
    zoo_paris = Zoo([donkey, tiger])
    zoo_london = Zoo([giraffe, mouse])
    zoo = Zoo([])
    assert zoo.__add__(zoo_paris,zoo_london) == [donkey, tiger, giraffe, mouse]
