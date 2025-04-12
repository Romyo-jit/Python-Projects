import os
import win32com.client

wdFormatPDF = 17

for i in os.listdir():
    print(i)

print()

in_file = os.getcwd() + '\\' + input("Write DOCX FIlename: ")
outfile = in_file[:-5] + '.pdf'

print("Converting to PDF...")

word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(outfile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()

print('Converted :)')
