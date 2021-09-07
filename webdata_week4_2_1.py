import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = int(input('Enter repeat how many times - '))
position = int(input('Enter position - '))

position = position -1
i = 0

print('Retrieving: ', url)

while i < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    i = i + 1

    tags = soup('a')
    tag = tags[position]
    url=tag.get('href', None)
    print('Retrieving: ', url)



#
# todo = list()
# visited = list()
# url = input('Enter - ')
# todo.append(url)
# count = int(input('How many to retrieve - '))
#
# while len(todo) > 0 and count > 0 :
#     print("====== To Retrieve:",count, "Queue Length:", len(todo))
#     url = todo.pop()
#     count = count - 1
#
#     print("===== Retrieving ", url)
#
#     try:
#         html = urllib.request.urlopen(url, context=ctx).read()
#     except:
#         print("*** Error in retrieval")
#         continue
#
#     soup = BeautifulSoup(html, 'html.parser')
#     visited.append(url)
#
#     # Retrieve all of the anchor tags
#     tags = soup('a')
#     for tag in tags:
#         newurl = tag.get('href', None)
#         if (newurl is not None):
#             todo.append(newurl)
