
from flask import Flask, render_template, request, jsonify, redirect, flash, url_for
from flask_pymongo import PyMongo


import helpers
import requests
import private

app = Flask(__name__)

app.config['MONGO_URI'] = private.database_url
app.secret_key = private.secret_key

mongo = PyMongo(app)

if __name__ == "__main__":
    app.run()


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/s/<path:url_key>')
def get_url(url_key):
    url_key = request.path[3:]

    urls_collection = mongo.db.urls

    valid_url = urls_collection.find_one({'url_key':  str(url_key)})
    if valid_url != None:
        return redirect(valid_url['original_url'])
    else:
        return 'Error'
        

@app.route('/short')
def short_url(short_url=None):
    return render_template('short-url.html', short_url= short_url)


@app.route('/short', methods=['POST'])
def short_api():

    url_result = ""

    if request.method  == 'POST':
        api_result = {}

        url = request.form['url']
        verify_url = helpers.valid_https(url)

        if verify_url == True:
            #Database collection
            urls_collection = mongo.db.urls

            new_url = urls_collection.find_one({'original_url': url})

            if new_url == None:
                #Short url key
                key = helpers.url_key()

                urls_collection.insert({'url_key': key, 'original_url': url})
                url_result = key
            else:
                key = new_url['url_key']
                url_result = key
            
        else:
            return 'Error'
    return redirect(url_for('short_url', short_url= url_result, original_url=url))