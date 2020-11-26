import xml.etree.ElementTree as ET

tree = ET.parse("sample.xml")

for i in tree.findall("food/price"):
    i.tag = "value"

tree.write("sampleOutput.xml")
