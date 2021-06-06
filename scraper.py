import urllib.request

fp = urllib.request.urlopen('URL HERE')
b = fp.read()

html = b.decode('utf-8')
fp.close()

f = open('indeed.txt', 'w', encoding='utf-8')

f.write(html)

f.close()