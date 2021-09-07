import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = int(input('Enter count - '))
position = int(input('Enter position - '))

for i in range(0, count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags

    tags = soup('a')
    print(tags)


# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# times = int(input('Enter no. of time to repeat - '))
# position = int(input('Enter position of link to retrieve - '))
#
# for i in range(0, times):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#
#
#
#     tags = soup('a')
#     print(tags)
#     identifiedtags = tags[position-1]
#     link = identifiedtags.get('href', None)
#     print('Retrieving: ', link)
#     tags = list()
