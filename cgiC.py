#!C:\Users\lost\AppData\Local\Programs\Python\Python36-32\python.exe

import cgi

 
print ("Content-Type: text/json\n\n")
fields = cgi.FieldStorage()
palavra = fields.getvalue('palavra')
url = fields.getvalue('url')



import requests, re, json
from bs4 import BeautifulSoup as Soup
r=requests.get(url)
c=r.content
a=Soup(c,"html.parser")
fs = a.find_all(text =re.compile(palavra))
data = {'total_string' : len(fs)}
json_str = json.dumps(data)
print (json_str)