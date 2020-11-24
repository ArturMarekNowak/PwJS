import os
listOfFiles = os.listdir('.')
for i in listOfFiles:
    name, ext = os.path.splitext(i)
    if ext == ".jpg":
        os.rename(i, name + ".png")

