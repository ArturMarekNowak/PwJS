password = "1234"

for i in range(3):
    userInput = input("Podaj haslo: ")

    if userInput == password:
        print("Haslo prawidlowe")
        break
    else:
        print("Haslo niepoprawne, zostaly %d szanse" % (2-i))


