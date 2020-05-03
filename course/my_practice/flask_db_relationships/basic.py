from models import db, Puppy, Owner, Toy

# db.create_all()  -  used if migration is not used
# flask db init, flask db migrate -m 'message', flask db upgrade


# Creating two puppies:

rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add the puppies to db:

db.session.add_all([rufus, fido])
db.session.commit()

# Check adding the puppies

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()  # all([0])
print(rufus)
rufus.report_toys()

# Create an owner object

print(f'Rufus id is {rufus.id}')
jose = Owner('Jose', rufus.id)

# Some toys for Rufus

chew = Toy('Chew toy', rufus.id)
ball = Toy('Ball', rufus.id)

db.session.add_all([jose, chew, ball])
db.session.commit()

# Grab Rufus after all the additions!

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()

