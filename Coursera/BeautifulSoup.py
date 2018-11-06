#this program reads a url and print the sum of all numbers in tha particular url
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numbers = []
for tag in tags:
    # Look at the parts of a tag
    numbers.append( int(tag.string))
print(sum(numbers))
