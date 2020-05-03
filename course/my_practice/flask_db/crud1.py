from base1 import db, Puppy


## Create ##

my_puppy = Puppy('Tobik', 1)
db.session.add(my_puppy)
db.session.commit()

## Read ##

all_puppies = Puppy.query.all() # list of puppy objects on the table
print(all_puppies)

# Select by id ##

puppy_one = Puppy.query.get(1)
print(puppy_one)

## Filters ##
puppy_tobik = Puppy.query.filter_by(name='Tobik').all()
print(puppy_tobik)

## Update ##

first_puppy = Puppy.query.get(1)
first_puppy.age = 7
db.session.add(first_puppy)
db.session.commit()

## Delete ##

second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


all_puppies = Puppy.query.all()
print(all_puppies)


