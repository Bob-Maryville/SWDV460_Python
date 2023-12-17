import xml.etree.ElementTree as ET

tree = ET.parse("C:/Users/bobba/OneDrive/Desktop/School/SWDV_460/catalog.xml")
root = tree.getroot()

for book in root.findall('book'):
    title = book.find('title').text
    print(title)

