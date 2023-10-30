import xml.etree.ElementTree as ET

t = ET.parse('burma14.xml')
r = t.getroot()
res = r.find('graph')
print(len(res.findall('vertex')))

