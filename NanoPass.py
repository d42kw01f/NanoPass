import string 
import random

class CreatPasswords:
    Letters = string.ascii_letters
    Numbers = string.digits
    SpecialChar = string.punctuation

    def __init__(self, length, UserInput):
        self.length = length
        self.UserInput = UserInput

    def TheMainOne(self):
        if self.UserInput == 1:
            TheConstant = CreatPasswords.Numbers + CreatPasswords.Letters + CreatPasswords.SpecialChar
        elif self.UserInput == 2:
            TheConstant = CreatPasswords.Numbers + CreatPasswords.Letters
        elif self.UserInput == 3:
            TheConstant = CreatPasswords.Letters
        else:
            raise ValueError('Wrong Input...')
        TheConstant = list(TheConstant)
        random.shuffle(TheConstant)
        random_password = random.sample(TheConstant,  k=self.length)
        TheRandPassword = ''.join(random_password)
        return TheRandPassword


if __name__ == '__main__':
    while True:
        try:
            TheLen = int(input("Enter the length of the password: "))
            print("\n\n1. Advanced Security Password")
            print("2. Medium Security Password")
            print("3. Low Security Password")
            UserOption = int(input("Enter the your options: "))
            The_Pass = CreatPasswords(TheLen, UserOption)
            ThePassword = CreatPasswords.TheMainOne(The_Pass)
            break
        except ValueError as e:
            print("Opps: Something went wrong!!\nLet's try this again...\n\n")
    print("\n\nYou are Password is: \n{}".format(ThePassword))
