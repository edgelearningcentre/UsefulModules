#! Python3
# to get data from PDF file
# To install PyPDF2 module  use this command in VS Code py -m pip install PyPDF2

import PyPDF2       # To import PyPDF2 module for read Pdf Files
pdfFileObject = open('python-guide.pdf','rb')   # open particular pdf file in rb mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObject) # To use PDF reader to read an object file
count = pdfReader.numPages      # to count number of pages in a single PDF document
output = ''                     # create an blank string file to store the extracted part
for i in range(0,count):        # start loop from 0 to length of total pages in a PDF
    page = pdfReader.getPage(i) # start reading using getPage one by one , i increments + 1
    output += page.extractText() # extract text and append blank output file
                                # += means increment one value like output + 1
print(output)