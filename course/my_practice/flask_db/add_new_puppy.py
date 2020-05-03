from pprint import pprint
from base1 import db, Puppy

all_puppies = Puppy.query.all()
pprint(all_puppies)

mikie = Puppy('Mikie', 7, 'doberman')
db.session.add(mikie)

sammy = Puppy.query.get(1)
sammy.breed = 'poodle'
db.session.add(sammy)

db.session.commit()

all_puppies = Puppy.query.all()
pprint(all_puppies)
