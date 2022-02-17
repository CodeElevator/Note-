from exceptions import *

print('My NoteBook')
print('Note: Do not reuse file names for text will be overwritten.')
import sys
exit=0
while exit!='y':
  m=input('Select an option: a)read your docs or b)write a doc or c)delete a doc,')
  def writes(): 
    title=input('Enter the title of this paper')
    mood = input('Write something: ')
    text_file = open(title,'w')
    text_file.write(mood)
    text_file.close()
  def read():
    inputFileName = input("Enter name of paper: ")
    try:
      inputFile = open(inputFileName, "r")
      for line in inputFile:
        sys.stdout.write(line)
    except FileNotFound:
      raise NoteNotFound("The notefile name was not found")
  def delete():
    import os

    print("Enter the Name of Paper: ")
    filename = input()
  
    os.remove(filename)
    print("\nPaper deleted successfully!")
  
    

    
  


  if m=='a':
    read()
  elif m=="b":
    writes()
  else:
    delete()

  
  exit=input('\nDo you want to exit, y/n')
sys.exit('Thank you' )
