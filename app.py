from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient(<MOGODB CONNECTION STRING>)
db = client.Heroku
col = db['resume']

@app.route('/')
def first():
    return render_template('index.html')

"""https://pythonhow.com/add-css-to-flask-website/  VISIT THIS FOR ADDING CSS FILES (STATIC FILES)"""

"""https://github.com/datademofun/heroku-basic-flask ADDITIONAL FILE FOR TUTORIALS"""


@app.route('/thanks', methods = ['POST'])
def second():
    if request.method == 'POST':
        posted_data = request.form
        email = posted_data['email']
        text = posted_data['text']
        name = (email.split("@"))[0]
        col.insert({
        "NAME":name,
        "E-MAIL":email,
        "COMMENT":text
        })
        return render_template('thanks.html',name=name)
    else:
        pass

if __name__ == '__main__':
    app.run("0.0.0.0",debug = True)
