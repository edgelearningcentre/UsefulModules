# Ask the user to keep busy person for hours
#! Python3 
    
import pyinputplus as pyip                                  # import module
while True:                                                 # infinite loop until condition is met
    prompt = 'Do You Know Python Language is powerful ?\n'     # prompt message
    response = pyip.inputYesNo(prompt)                      # call YesNo with prompt variable
    if response == 'no':                                    # checking condition
        print('Thank you. Have a nice day.')                # print message
        break                                               # break the infinite loop 
