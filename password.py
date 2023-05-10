import random
import string
def password_gen(length, charset=None):

    if not charset:
        charset = string.ascii_letters + string.digits + "@!"
    password = "".join(random.choices(charset, k=int(length)))
    return password



def is_strong_password(password):

    return True # Altere isso para retornar True ou False com base na sua lógica de verificação.

charset = string.ascii_lowercase + string.digits
password = password_gen(8, charset=charset)




password = password_gen(10)
if is_strong_password(password):
    print("Senha forte!")
else:
    print("Senha fraca.")

def password_gen(size):
    all_letters = string.ascii_letters

    lower = all_letters[0:len(all_letters)//2]  # lowercase letters

    upper = all_letters[len(all_letters)//2:]  # uppercase letters

    numbers = string.digits  # numbers

    symbols = string.punctuation  # symbols

    mixed = lower + upper + numbers + symbols

    length = int(size)

    password = random.sample(mixed, length)

    password = "".join(password)

    return password
