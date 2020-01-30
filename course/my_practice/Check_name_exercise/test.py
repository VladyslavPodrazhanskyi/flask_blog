class Cat():
    def __init__(self, age, name, paws=4):
        self.age = age
        self.name = name
        self.paws = paws



my_cat = Cat(5, 'Barsik', paws=3)
print(my_cat.paws)
my_cat.paws = 3
print(my_cat.paws)

