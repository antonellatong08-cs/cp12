import random

uppercase = 'qwertyuiopasdfghjklzxcvbnm'
lowercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
digits = '0123456789'
special = '!@#$%^&*()'
total = uppercase + lowercase + digits + special
password = ""
for i in range(20):
    password += random.choice(total)
print(password)