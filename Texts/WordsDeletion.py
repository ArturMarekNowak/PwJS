file = open("srcForFirstScript/foo.txt")

text = file.read().replace(" się", "").replace(" oraz", "").replace(" nigdy", "").replace(" dlaczego", "").replace(" i ", " ")
file.close()

print(text)
