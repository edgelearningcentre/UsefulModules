#! Python3
# To validate the input data entered by an user for specific
# Introducing PyInputPlus Third Party Module
# py -m pip install PyInputPlus
# import pyinputplus as ip
# Age =ip.inputNum("Enter your age ")
# print(f"Great !! You are {Age} years old.")

"""
PyInputPlus has following functions
inputStr()
inputNum()
inputChoice()
inputMenu()
inputDatetime()
inputYesNo()
inputBool()
inputEmail()
inputFilepath()
inputPassword()
"""

# Introducing inputCustom() function for passing a validation 
"""
Write a function to perform your own custom validation logic
by passing the function to inputCustom().
"""
# User to enter a series of digits that squares up to 20.
# Steps to Create and simply follow the below instructions
"""
1. Accepts a single string argument that has entered by User.
2. Raise an exception if the string fails validation
3. Returns None if inputCustom() should return the string unchanged
4. Return a value if inputCustom() should return a different string
from the one user entered
5. Is passed as the first argument to inputCustom()
"""
# Enter number below 20.
import pyinputplus as pyip      # import module 
def squareNum(num):             # define function with argument num
    num = int(num*num)          # calculate square of input number num x num 
    print(f'The value of num is  {num} . Congratulations')  #
    if num >=400:               # if num is >400 it will raise exception with comment in it.
        raise Exception ('The entered number is out of scope !! please enter number less than or equal to 20')
        return int(num)         # return the number ; int(num) converts number into integer

squareNum(5)    # calling of function 5 * 5 = 25, is less than condition i.e. 400
squareNum(10)   # if square of numbers is less than 400, it will not raise an exception
squareNum(15)
squareNum(20)
squareNum(25)   # result is 625, it will raise an exception. It increases the condition 
