import os

path = 'a'

def ls_R(catalog):
    listOfFiles = sorted(os.listdir(catalog))
    size = len(listOfFiles)
    for i in range(size):
        if os.path.isdir(catalog + '/' + listOfFiles[i]):
            ls_R(catalog + '/' + listOfFiles[i])
    print("Catalog %s" % catalog)
    print(os.listdir(catalog))

ls_R(path)    
