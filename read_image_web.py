#read and save a image from web

import urllib.request, urllib.parse, urllib.error
img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand=open('hai.jpg','wb')
fhand.write(img)
fhand.close()
