#pip install argon2-cffi

from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("password")

with open("hash.txt", "w") as f:
    f.write(hash)
    
print("Hash saved to hash.txt")

with open("hash.txt", "r") as f:
    hash = f.read()
    password = input("Enter password: ")
    try:
        ph.verify(hash, password)
        print("Password is correct")
    except:
        print("Password is incorrect")