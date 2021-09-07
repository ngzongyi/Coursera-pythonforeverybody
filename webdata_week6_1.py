import urllib.request, urllib.parse, urllib.error
import json
from bs4 import BeautifulSoup


url = input('Enter location: ')
data = urllib.request.urlopen(url).read().decode()

info = json.loads(data)

print('Retrieving ', url)
print('Retrieved', len(data), 'characters')

count = 0
sum = 0

for item in info['comments']:
    sum = sum + int(item['count'])
    count += 1

print('Count: ', count)
print('Sum: ', sum)




#
# import json
#
# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''
#
# info = json.loads(data)
# print('User count:', len(info))
#
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])
