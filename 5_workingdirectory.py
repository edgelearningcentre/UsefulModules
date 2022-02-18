#! Python 3 
# How to check and change working directory in Python
from pathlib import Path
import os
print(Path.cwd())
print(Path.home())

"""
Difference between Relative and Absolute Path
There are two methods to specify file path
Absolute Path: Start with the root folder
Relative Path: Relative to the current working directory
"""
# To run this program just uncomment the  lines 16 and 17  and run and then uncomment  21 and 22
                                                    # create new folders 
# import os
# os.makedirs('C:\\PythonScripts\\Basics')            # it will create main folder named PythonScripts
#                                                     # # and Basics folder inside the PythonScripts Folder

#                                                     # To make a directory from a Path Object
# from pathlib import Path                            # import path to make an directory on specific path
# Path(r'C:\\Users\\neerajjulka\\Basics1').mkdir()    # it will create folder named Basics1 in the neerajjulka

# Path.cwd()                                            # it shows the actual path where you have saved the working directory
# Ab = Path.cwd().is_absolute()                         # Ab named variable is saving the output
# print(Ab)                                             # Output of this shows path is Absolute (True) or Relative (False)

ActualPath = Path('C:/Users/PythonScript/document.txt')

# Getting different parts of a file
ActualPath_Anchor = ActualPath.anchor
print(ActualPath_Anchor)

ActualPath_Parent = ActualPath.parent
print(ActualPath_Parent)

ActualPath_Name = ActualPath.name
print(ActualPath_Name)

ActualPath_Stem = ActualPath.stem
print(ActualPath_Stem)

ActualPath_Suffix = ActualPath.suffix
print(ActualPath_Suffix)

ActualPath_Drive = ActualPath.drive
print(ActualPath_Drive)

# The parents attribute evaluates to the ancestors folder of given path
# Just change [0] value to get all ancestors of particular path
Path.cwd()
print(Path.cwd().parents[0])