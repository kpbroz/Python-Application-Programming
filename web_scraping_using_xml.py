import xml.etree.ElementTree as ET
data='''
<person>
<name>chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="YES"/>
</person>'''
tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
