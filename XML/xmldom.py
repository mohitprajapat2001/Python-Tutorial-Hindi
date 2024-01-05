from xml.dom import minidom

tree = minidom.parse("myxml.xml")

# tagname = tree.getElementsByTagName('address')[0]
# # print(tagname.firstChild.data)
# # for i in tagname:
# #     print(i.firstChild.data)
# tagname.firstChild.data = "Chennai"


tagname = tree.getElementsByTagName('age')

print(len(tagname))


