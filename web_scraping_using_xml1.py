import xml.etree.ElementTree as ET

input='''
<stuff>
    <users>
        <user x="1">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="2">
            <id>002</id>
            <name>KP</name>
        </user>
    </users>
</stuff> '''

stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('User count: ',len(lst))

for item in lst:
    print('Name: ',item.find('name').text)
    print('Id: ',item.find('id').text)
    print('Attribute: ',item.get('x'))
