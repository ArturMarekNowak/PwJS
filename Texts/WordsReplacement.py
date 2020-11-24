file = open("srcForFirstScript/foo.txt")

text = file.read()
print(text)
text = text.replace(" nigdy ", " prawie nigdy ").replace(" dlaczego ", " czemu ")

text = text.split()

for i in range(len(text)):
    if text[i] == "i":
        text[i] = "oraz"
    elif text[i] == "oraz":
        text[i] = "i"

file.close()

text = " ".join(text)

print(text)
