import secrets
import string
import requests

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

def password_generator(pwd_length=8):
    password_string = ''
    while True:
      for i in range(pwd_length):
        password_string += ''.join(secrets.choice(alphabet))

      yield password_string

print(next(password_generator()))
print(next(password_generator()))

def citation_generator():
    get_req = requests.get("https://zenquotes.io/api/random")
    data = get_req.json()
    yield (f"Citat: {data[0]['q']} \n"
           f"A: {data[0]['a']}\n")

print(next(citation_generator()))
print(next(citation_generator()))
print(next(citation_generator()))
