#!/bin/python3


#PASSWORD GENERATOR USING PYTHON

#It’s important to protect your personal information online, and in this project you’ll create a program to generate passwords for you.

#The passwords will be random, so no one will be able to guess them!
#This program make use of the string library.

from string import letters,digits,punctuation
from random import choice

number = input('Enter number of password to generate : ')
number = int(number)

length = input('Enter length of each password :')
length = int(length)

char = letters+digits+punctuation
print(number,'Passowrds of length ',length,'are :\n')

for i in range(number):
  for j in range(length):
    print(choice(char),end='')
  print()
