import json

with open("sample.json") as jsonFile:
    data = json.load(jsonFile)
    temp = data["Obywatele"]

    print(json.dumps(data, indent = 4))

while True:
    print('''
    What do we do?
    d - delete record
    a - add record
    p - print all records
    Insert action: ''', end = '')
    action = input()

    if action == "a":

        newCitizen = dict.fromkeys(["PESEL", "imie", "nazwisko", "adres", "telefon"])

        for i in newCitizen:
            print("Podaj ", end = '')
            print(i, end = '')
            print(": ", end = '')
    
        rawInput = input()
        newCitizen[i] = rawInput 
    
        print(newCitizen)

        temp.append(newCitizen)

        with open("sample.json", 'w') as jsonFile:
            json.dump(data, jsonFile, indent = 4)

    if action == "d": 
        print("Enter PESEL to delete a record: ", end = '')
        delRecord = input()

        for i in range(len(temp)):
            print(temp[i])
            if temp[i]["PESEL"] == delRecord:
                temp.pop(i)
                break

        with open("sample.json", 'w') as jsonFile:
            json.dump(data, jsonFile, indent = 4)

    

    if action == "p":
        with open("sample.json") as jsonFile:
            data = json.load(jsonFile)
            temp = data["Obywatele"]

            print(json.dumps(data, indent = 4))

    print("Continue? [y/n]:", end = '')
    cont = input()
    if cont == "y":
        pass
    elif cont == "n":
        break
    else:
        print("Incorrect command")
        break

