from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'
password_2 = 'supersecretpassword'
hashed_password = bcrypt.generate_password_hash(password=password)
hashed_password_2 = bcrypt.generate_password_hash(password=password_2)

check = bcrypt.check_password_hash(hashed_password, password_2)

print('hashed_password:', hashed_password)
print('hashed_password_2:', hashed_password_2)
print(check)