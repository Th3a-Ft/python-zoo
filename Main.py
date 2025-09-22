from Animal import Animal
from Bird import Bird
from Serpent import Snake

animal = Animal(25,12)

print(animal.weight, animal.height)

snake = Snake(10,120)
print(snake.move())

bird = Bird(10, 23,2500)
print(bird.move())

ani = Animal(74,25)
print(str(ani))