print("Podaj imie, nazwisko oraz rok urodzenia: ", end ='' )
rawInput = input()

rawInput = rawInput.split()

print("masz na imie %s %s i urodziles/as sie w roku %s" % (rawInput[0], rawInput[1], rawInput[2]))

