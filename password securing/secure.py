import string
secure = (('a','@'),('i','!'),('o','0'),('@','&'),('_','-',),('e',';'),('c','k'),('s','$'))
shift = 8

def secure_password(password):
    # Cesar encryption
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    password = password.translate(table)

    # password = password.lower()
    for a,b in secure:
        password = password.replace(a,b)
    return password


if __name__ == "__main__":
    password = input("Please enter your password\n")
    password = secure_password(password)
    print(f"Your secured password is {password}")