#! Python3
# To validate the input data entered by an user for specific.
while True:                                                 # while condition
    Marks = input("Enter Student Marks:")                   # get input from user for marks
    try:                                    # use try and except to continue program 
        Marks = int(Marks)                  # convert input value into integer using int
    except:                                 # except gives some specific condition
        print("Please enter only numbers")  # print message enter only numbers
        continue                            # continue with this exception
    if Marks <= 33:                         # condition if marks is less than equal to 33
        print('Better Luck next time !! You Failed the exam')
    else:
        print('Congratulations !! You passed the exam')
    break                                   # break the infinite while loop
print(f'You secured {Marks} marks out of 100 .')