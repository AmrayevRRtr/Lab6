ex1
import os
path = 'g:\\mypath\\'
print("Directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("Directories and files:")
print([ name for name in os.listdir(path)])

ex2
import os
print('Exist?', os.access('mypath.docx', os.F_OK))
print('Readable?', os.access('mypath.docx', os.R_OK))
print('Writable?', os.access('mypath.docx', os.W_OK))
print('Executable?', os.access('mypath.docx', os.X_OK))

ex3
import os
path = r'g:\\mypath\\a.txt'
print("Exist?", os.path.exists(path))
if os.path.exists(path):
    print("File name:", os.path.basename(path))
    print("Dir name:", os.path.dirname(path))

ex4
def length_of_file(name):
        with open(name) as file:
            count = sum(1 for line in file)     
        return count
print("Number of lines",length_of_file("a.txt"))

ex5
mylist = ['one', 'two', 'three', 'four', 'five']
with open('b.txt', 'w') as file:
    for i in mylist:
        file.write(i)
res = open('b.txt')
print(res.read())

ex6
import string, os
for i in string.ascii_uppercase:
   with open(i + ".txt", "w") as f:
       f.writelines('Success! Created')

ex7
from shutil import copyfile
copyfile('a.py', 'b.py')

ex8
import os
if os.path.exists("a.txt"):
    os.remove('a.txt')
else:
    print("The file does not exist")