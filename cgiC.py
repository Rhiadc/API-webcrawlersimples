

import requests, re, json, cgi
from bs4 import BeautifulSoup as Soup
 
print ("Content-Type: text/json\n\n")
fields = cgi.FieldStorage()
word = fields.getvalue('palavra')
url = fields.getvalue('url')
totalRequests=requests.get(url)
totalContent=totalRequests.content
parsedContent=Soup(c,"html.parser")
fs = parsedContent.find_all(text =re.compile(word))
data = {'total_string' : len(fs)}
json_str = json.dumps(data)
return json_str
