import time
import os
import shutil

path=input("Enter Folder Path: ")
day=time.time()
if os.path.exists(path)==True:
    print("Path Exists, Continuing")
print(os.walk(path))
print(os.path.join(path, os.walk(path)))