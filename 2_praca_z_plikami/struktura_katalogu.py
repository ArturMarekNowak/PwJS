import os

path = 'a'

def ls_R(catalog):
    #i = 0
    listOfFiles = sorted(os.listdir(catalog))
    size = len(listOfFiles)
    #print("Current catalog: %s" % catalog)
    #if os.path.isdir(catalog):
    for i in range(size):
        if os.path.isdir(catalog + '/' + listOfFiles[i]):
            ls_R(catalog + '/' + listOfFiles[i])
    print("Catalog %s" % catalog)
    print(os.listdir(catalog))
        


ls_R(path)    
