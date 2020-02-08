from base import db,Puppy

###########################
###### CREATE ############
#########################
my_puppy = Puppy('Rufus', 5)
second_rufus = Puppy('Rufus', 1)
db.session.add_all([my_puppy, second_rufus])
db.session.commit()

###########################
###### READ ##############
#########################
# Note lots of ORM filter options here.
# filter(), filter_by(), limit(), order_by(), group_by()
# Also lots of executor options
# all(), first(), get(), count(), paginate()

all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)
print('\n')
# Grab by id
puppy_one = Puppy.query.get(1)
print(puppy_one)
print(puppy_one.age)
print('\n')
# Filters
puppy_rufus = Puppy.query.filter_by(name='Rufus').all() # Returns list
print(puppy_rufus)
print('\n')
###########################
###### UPDATE ############
#########################

# Grab your data, then modify it, then save the changes.
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


###########################
###### DELETE ############
#########################
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


# Check for changes:
all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)




# from base import db, Puppy
#
# ### Create ####
#
# bob = Puppy('Bob', 7)
# tobik = Puppy('Tobik', 11)
#
# db.session.add_all([bob, tobik])
# db.session.commit()
#
# print(tobik.id)
#
# ### Read ###
#
# all_puppies = Puppy.query.all()
# print(all_puppies)
#
# puppy_two = Puppy.query.get(2)
# print(puppy_two)
#
#
# # puppy_bob = Puppy.query.filter_by(id=2)
# # print(puppy_bob)
# puppy_sam = Puppy.query.filter_by(name='Sammy') # Returns list
# print(puppy_sam)
#
#
# ########################
# ###### Update ##########
# ########################
#
# puppy_one = Puppy.query.get(1)
# print(puppy_one.age)
# puppy_one.age = 18
#
# db.session.add(puppy_one)
# db.session.commit()
#
# ########################
# ###### DELETE ##########
# ########################
#
# puppy_fourth = Puppy.query.get(4)
# db.session.delete(puppy_fourth)
# db.session.commit()
#
# all_puppies = Puppy.query.all()
# print(all_puppies)