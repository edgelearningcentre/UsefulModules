# to install  just write this command in the terminal without quotes
# "pip install pyperclip"

# PyPerClip  module has copy() and paste() functions that can send text to and 
# recieve text from your computer's clipboard.

import pyperclip
pyperclip.copy('PyPerClip has only copy and paste functions')
pyperclip.paste()

"""
First Time Error
Traceback (most recent call last):
  File "c:/Users/UsefulModules/1_PyPerClip.py", line 7, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'
"""