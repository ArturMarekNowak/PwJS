file = open("srcForFirstScript/foo.txt")

text = file.read()
print(text)

text = text.split()

for i in range(len(text)):
    if text[i] == "i":
        text[i] = "oraz"
    elif text[i] == "oraz":
        text[i] = "i"
    elif text[i] == "nigdy":
        text[i] = "prawie nigdy"
    elif text[i] == "dlaczego":
        text[i] = "czemu"

file.close()

text = " ".join(text)

print(text)
