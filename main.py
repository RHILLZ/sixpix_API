from crypt import methods
from flask import Flask, jsonify, request
from pexel_lib import *
import json


app = Flask(__name__)

# Global variables
nextpage = ''
imgs = []


@app.route('/')
def home():
    return 'Six Pix is running!'


@app.route('/search/<query>')
def search(query):
    global nextpage
    global imgs
    images, next_url, page = searchQuery(query=query)
    nextpage = next_url
    imgs = images
    return jsonify({'images': images, 'next_page': next_url, 'page': page})


@app.route('/next')
def goToNext():
    global nextpage
    global imgs
    images, next_url, page = goToNextPage(nextpage)
    nextpage = next_url
    imgs = images
    return jsonify({'images': images, 'next_page': next_url, 'page': page})


@app.route('/save/<filename>/<index>')
def save(filename, index):
    result = saveImage(filename=filename, image=imgs[int(index)])
    return result


if __name__ == "__main__":
    app.run(port=5500, host='0.0.0.0', debug=True)
