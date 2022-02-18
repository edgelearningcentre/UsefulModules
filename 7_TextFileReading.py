#! Python3 
"""
Text Files contains only text characters, exclude all other information like font etc.
.txt and .py extensions are examples of text files and editable in Notepad.
Docx Files, PDF Files, Images, Excel Files and .exe files are examples of Binary Files.
"""
from pathlib import Path
P = Path('document.txt')
P.write_text("Hello Everyone !! to the Edge Learning Centre \nIn this you will learn Python by solving problems")
#print(P.read_text())

docFile = open(P)               # to open a file and will get path from variable P
#print(docFile)

docContent = docFile.read()     # to read the file and print its contents
print(docContent)

doc1_File = open('document1.txt','w')       # open document.txt file with write mode
print(doc1_File.write('You can just run these codes and try it by yourself by solving problems'))

doc1_File = open('document1.txt')
content = doc1_File.read()
print(content)