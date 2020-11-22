file = open("srcForFirstScript/foo.txt")

text = file.read().replace(" nigdy ", " prawie nigdy ").replace(" dlaczego ", " czemu ")
file.close()

print(text)
