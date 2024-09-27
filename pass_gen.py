import random
import string
length=int(input("enter thye length of password"))

chare=string.ascii_letters+string.digits+string.punctuation
password="".join(random.choice(chare) for i in range(length))
print(password)