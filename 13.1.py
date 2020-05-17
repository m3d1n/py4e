import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

suma=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_444621.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
#print('User count:', len(lst))

for item in lst:
    #print('Name', item.find('name').text)
    x=int( item.find('count').text)

    suma=suma+x

print(suma)
