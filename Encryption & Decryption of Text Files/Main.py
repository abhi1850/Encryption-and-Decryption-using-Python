from Caesar_Cipher import Caesar_Cipher
from Brute_Force import Brute_Force
from Autokey_Cipher import Autokey_Cipher
#from aes import *

def operation(choice):
    operations = [Caesar_Cipher, Brute_Force, Autokey_Cipher]
    operations[choice - 1]()

def get_choice():
    choice = int(input("Enter the choice: "))
    return choice

if __name__ == "__main__":
    print("Please enter the method that you want to use:")
    print("Brute Force is the special case of Caesar Cipher in which all the possible decrypted messages are displayed")
    print('''
          1. Caesar Cipher
          2. Brute Force
          3. Autokey Cipher''')

    choice = int(input("Enter the choice: "))
    valid_choices = [1, 2, 3, 4]
    if choice in valid_choices:
        operation(choice)
    else:
        while choice not in valid_choices:
            print("Entered choice is not in the range of {1-4}.")
            choice = get_choice()
        operation(choice)
