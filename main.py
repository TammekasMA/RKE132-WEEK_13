from animal import Animal, Cat, Dog

my_cat = Cat("Fluffy")
my_dog = Dog("Rex")
neighbours_dog = Dog("Chilly")

my_dog.sees(neighbours_dog)  # koer näeb koera
my_cat.sees(my_dog)          # koer näeb kassi → haugub