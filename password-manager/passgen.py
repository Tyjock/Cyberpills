import random
import string

def generate_password(lenght: int = 32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(lenght))
    return password 

password = generate_password()
print(f"Generated password: {password}")
