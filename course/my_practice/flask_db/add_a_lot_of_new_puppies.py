from random import choice
from base import db, Puppy
names = ['Stella', 'Sharik', 'Angella', 'Barbos',
         'Dick', 'Mike', 'John', 'Quickie']

ages = list(range(1, 12))

puppies = [Puppy(choice(names), choice(ages)) for _ in range(30)]

for puppy in puppies:
    db.session.add(puppy)

db.session.commit()