import os
import shutil
try :
    shutil.rmtree("files") 
except FileNotFoundError :
    pass

n = int(input())
path = os.getcwd()

os.mkdir("files")
os.chdir("files")
for i in range(n) :
    os.mkdir("f" + str(i+1))
print(sorted(os.listdir()))
    
os.rename("f1", "folder1")
print(sorted(os.listdir()))

os.rmdir("folder1")
print(sorted(os.listdir()))

os.chdir(path)
shutil.rmtree("files")