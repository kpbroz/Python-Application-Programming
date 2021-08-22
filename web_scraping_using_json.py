import json

data='''
{
"name":"Chuck",
"phone":{
"type":"intl",
"number":"94498499"
},
"email":{
"hide":"yes"
}
}'''

info=json.loads(data)
print('Name: ',info["name"])
print('Hide: ',info["email"]["hide"])
