# Creating random password with chars
import random
chars = 'asdfqwerzxcv'
pass_length = random.choice((10, 20))
password = ''
for i in range(pass_length):
  password += random.choice(chars)
print(password)