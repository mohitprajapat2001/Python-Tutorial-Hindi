import xmltodict

file = open("myxml.xml", "r")
data = file.read()
xmldict = xmltodict.parse(data)
print(xmldict["mydata"]['employee'][1]['name'])
