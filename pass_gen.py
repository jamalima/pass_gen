#!/usr/bin/env python
#
# Author: Maryam Jamali, 1397
# Description: Password Generator
#
import random
import string

class PassGen:

    def __init__(self):
        self.len = int(input ("Please enter the length for password: "))

    def generate(self):
        passwords = []
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        for i in range(10):
            password = ''
            for c in range(self.len):
                password += random.choice(chars)
            passwords.append(password)
        return passwords

if __name__ == "__main__":
    enter = input ("Press enter to start or Q to quit !")
    if enter.lower == 'q':
        exit(0)
    pass_gen = PassGen()
    passwords = pass_gen.generate()
    print ("My Suggestion is:")
    print ("\n".join(passwords))
    exit(0)