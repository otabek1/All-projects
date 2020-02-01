import hashlib
import requests

user_password = input("Enter your password for checking: ")
url = "https://api.pwnedpasswords.com/range/"
times = 0
hashed_password = hashlib.sha1(user_password.encode()).hexdigest()
get = requests.get(url + hashed_password[:5])
# print(hashed_password[5:].upper())
for te in get.text.split("\n"):
    te2 = te.split(":")
    if te2[0] == hashed_password[5:].upper():
        times = te2[1]
        break


print("Number of hacks for your password  ", end="")
print(times, end="")
# print("jasl")
# print("Your password is good-enough. Continue using it")
