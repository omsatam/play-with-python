import string
import random

if __name__ == "__main__":
    #for lowercase letters
    lower = string.ascii_lowercase
    #for uppercase letters
    upper = string.ascii_uppercase
    #for digits
    digits = string.digits
    #for special characters
    symbols = string.punctuation

    try:
        pass_len = int(input('Enter the password length: '))
        password = []
        password.extend(list(lower))
        password.extend(list(upper))
        password.extend(list(digits))
        password.extend(list(symbols))

        random.shuffle(password)
        password = ''.join(password[0:pass_len])
        print(password)
    except:
        print('Please enter a valid number')