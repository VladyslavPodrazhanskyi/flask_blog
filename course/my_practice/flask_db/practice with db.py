from base1 import db, Puppy

second_pup = Puppy.query.get(2)
print(second_pup)

second_created = Puppy('Igor', 4, 'poodle')
