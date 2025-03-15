#Open files using thr open() func. expects atleast one argument.
#returns a file object
with open('myfile.txt') as f:
    text=f.read()
print(text)
#By using with open(), the opened file resource will only be available in the indented block of code
#It makes sure that the file is closed.
'''
    :.'r'=read mode
    :.'w'=write mode
    :.'x'=create a new file and open it for writing
    :.'a'=open for writing, append to the end of the file if it exists already
    :.'t'=Text mode,can be used in combination with rwxa
    :.'b'=binary mode, can be used with rwxa
    :.'+'=open a disk file for updating
'''
with open('test_test.txt','w') as f:
    for i in range(1,5):
        f.write(f'Number {i}\n')
with open('test_test.txt','r') as f:
    print(f.read())
with open('test_test.txt','a') as f:
    for i in range(5,8):
        f.write(f'Append number {i}\n')
with open('test_test.txt') as f:
    print(f.read())
with open('test_test.txt') as f:
    lines=list(f)#same as lines=f.readlines()
#to read line-by-line:
'''
with open('test_test.txt','r') as f:
        for line in f:
            print(line)       
'''
import os
if os.path.isfile('test_test.txt'):
    print('It is a file')
if os.path.isdir('/python'):
    print("It's a directory")
os.mkdir('mydir')
os.remove('test_test.txt')
os.rename('myfile_txt','renamed_myfile.txt')
import shutil
#shutil.move('from_path','to_path')can move files between systems as well.
#shutil.copy()
#shutil.copytree()
#shutil.rmtree()
''' 
FILE TYPES:
        – : regular file
        d : directory
        c : character device file
        b : block device file
        s : local socket file
        p : named pipe
        l : symbolic link
'''