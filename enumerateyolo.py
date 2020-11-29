from pathlib import Path
import os
import sys

# this function is used to transform windows path to linux path
def pathtolinux(path, limit):
    result = ""
    s1 = path.split("\\")
    s2 = s1[len(s1) - limit : len(s1)]
    for i in s2:
        i = i.replace(':', "")
        result = result + i + "\\"
    s = list(result)
    s[-1] = ""
    return "".join(s)

argumentsLength = len(sys.argv) 
limit_path = 3
save_path = ""
data_path = ""
print(argumentsLength)
if argumentsLength >= 2:
    data_path = sys.argv[1]
    if argumentsLength >= 3:
        save_path = sys.argv[2]
        
        if argumentsLength >= 4:
            limit_path = int(sys.argv[3]) # e.g. 2 - "C:/Windows/System32" - /Windows/System32
            
        print("The limiter is {0}.".format(limit_path))
    else:
        save_path = "{0}\{1}".format(data_path, "dataset.txt")
        print("No save path was specified. The file is going to be saved here: {0}".format(save_path))
    
else:
    print("No data path was specified.\n https://github.com/SeeenyaOhar/enumerateyolo")
    exit(1)




# GET DATA
data = []
with os.scandir(data_path) as files:
    for i in files:
        print(i)
        if not i.is_dir():

            split = i.path.split(".")
            fileDirectory = "".join(split[0 : -1])
            if split[-1] == "txt":
                jpg_path = fileDirectory + ".jpg"
                if pathtolinux(jpg_path, limit_path) not in data:
                    if (os.path.exists(jpg_path)):
                        data.append(pathtolinux(jpg_path, limit_path))
                        print("append")

            elif split[-1] == "jpg":
                txt_path = fileDirectory + ".txt"
                if pathtolinux(i.path, limit_path) not in data:
                    if (os.path.exists(txt_path)):
                        data.append(pathtolinux(i.path, limit_path))
                        print("append")
print(data)
with open(save_path, mode='w') as file:
    for i in data:
        file.write(i + "\n")
print("File created. The name of file: " + save_path)

        
    
# TRANSFER TO YOLO VERSION
# SAVE HERE
    
