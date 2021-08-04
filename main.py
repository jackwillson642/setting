import os
import shutil
import time

exefile = input("Enter path to the exe:\n")
source = os.path.split(exefile)[0]
settings = input("Enter path to folder containing textfiles:\n")

# If you wish to hard code the paths of exefile and textfiles directory
# exefile = ""
# source = os.path.split(exefile)[0]
# settings = ""

print("The path to the directory containing exe file: " + source)
print("The path to the directory containing text files: " + settings)
print("\n\n")

time.sleep(1)

listfiles = os.scandir(settings)

# testfiles is a list containing all the txt files in the settings directory
textfiles = []
for file in listfiles:
    if file.is_file() and file.name.split('.')[-1] == "txt":   # Checks if the contents of the directory is a file and has a txt extention
        textfiles.append(file.name)

for filename in textfiles:
    src = os.path.join(settings, filename)
    dest = os.path.join(source, filename)
    shutil.copyfile(src, dest)  # Copy the text file to the source directory
    print(f"{src} copied to {dest}\n")
    time.sleep(1)
    os.system(exefile)  # Execute the program

input("Press Enter to exit")
