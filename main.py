import os
import shutil

listfiles = os.scandir('./settings/')

# testfiles is a list containing all the txt files in the settings directory
textfiles = []
for file in listfiles:
    if file.is_file() and file.name.split('.')[-1] == "txt":   # Checks if the contents of the directory is a file and has a txt extention
        textfiles.append(file.name)


# exefile = input("Enter path to the exe:\n")
# source = os.path.split(exefile)[1]
# settings = input("Enter path to folder containing textfiles:\n")

exefile = "/home/jack/programming/python/new_project/src/test.exe"
source = os.path.split(exefile)[0]
settings = "/home/jack/programming/python/new_project/settings/"

for filename in textfiles:
    src = os.path.join(settings, filename)
    dest = os.path.join(source, filename)
    shutil.copyfile(src, dest)  # Copy the text file to the source directory
    print(src + " copied to " + dest)
    os.system(exefile)  # Execute the program
