from flask import Flask
from flask import render_template
from flask import request
import requests, re, json
from bs4 import BeautifulSoup as Soup

app = Flask(__name__)


@app.route('/')
def index():
	return "Webcraler simples"

@app.route('/myprofile')
def showmyprofile():
    return render_template('myprofile.html')


@app.route('/addprofileform')
def addprofileform():
    return render_template('myprofileform.html')


@app.route('/addprofile')
def addprofile():
    palavra = request.args.get('palavra')
    url = request.args.get('url')
    r = requests.get(url)
    c = r.content
    a = Soup(c, "html.parser")
    fs = a.find_all(text=re.compile(palavra))
    data = {'total_string': len(fs)}
    json_str = json.dumps(data)
    return render_template('myprofile.html', palavra=json_str)


if __name__ == '__main__':
    app.run()