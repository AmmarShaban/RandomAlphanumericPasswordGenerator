import random
def uppercaseletter():
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    return random.choice(UPCASE_CHARACTERS)
def lowercaseletter():
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    return random.choice(LOCASE_CHARACTERS)
def digit():
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return random.choice(DIGITS)
def symbol():
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '/', '<' ,'>','*', '(', ')']
    return random.choice(SYMBOLS)
def main():
    CHARACTER_NUM=int(input("Enter Number of Characters in Password:"))
    NUM=0
    PASSWORD=""
    for i in range(CHARACTER_NUM):
        NUM=random.randint(1,4)#so if the character is a upper/lower case letter or number or symbol is random for every character
        if NUM == 1:
            PASSWORD+=uppercaseletter()
        elif NUM == 2:
            PASSWORD+=lowercaseletter()
        elif NUM == 3:
            PASSWORD+=digit()
        elif NUM == 4:
            PASSWORD+=symbol()
    print(PASSWORD)
main()

