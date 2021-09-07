import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#xml url http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_1285010.xml

url = input('Enter URL: ')
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

print()
print(xml)

counts = tree.findall('.//count')


print(counts)
sum = 0
for item in counts:
    sum = sum + int(item.text)

print(sum)

#
# print "Count: " + str(len(counts))
#
# accumulator = 0
#
# for count in counts:
#     accumulator += int(count.text)
#
#     print "Sum:" + str(accumulator)
