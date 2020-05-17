import urllib.request, urllib.parse, urllib.error
import json
import ssl

suma=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=' http://py4e-data.dr-chuck.net/comments_444622.json'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
info = json.loads(data)
print('User count:', len(info['comments']))
x=(info['comments'])
for item in x:

    s=int(item['count'])
    suma=suma+s
print(suma)
