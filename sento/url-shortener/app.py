import sqlite3
# import json
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os


def getDbConnection():
    connection = sqlite3.connect('urlShortener.db')
    connection.row_factory = sqlite3.Row
    return connection

# SECRET_KEY = os.getenv('FLASK_SECRET', '902h349r0p78w2q34ddqwere')
app = Flask(__name__)
app.config['SECRET_KEY'] = "902h349r0p78w2q34ddqwere"

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

@app.route('/', methods=('GET', 'POST'))
def index():
    connection = getDbConnection()

    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('The URL is required!')
            return redirect(url_for('encode'))

        urlData = connection.execute('INSERT INTO urls (original_url) VALUES (?)',
                                (url,))
        connection.commit()
        connection.close()

        urlId = urlData.lastrowid
        hashid = hashids.encode(urlId)

        return render_template('index.html', short_url=hashid)

    return render_template('index.html')

@app.route('/encode/<id>')
def encode(id):
    original_id = hashids.decode(id)
    if original_id:
        shortUrl = request.host_url + id
        return jsonify(
            shortUrl=shortUrl
        )
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))

# with app.test_client() as testClient:
#     response = testClient.get('/encode/5qW2')
#     jsonResponse = json.loads(response.get_data(as_text=True))
#     assert response.status_code == 200
#     assert jsonResponse['shortUrl'] == 'http://localhost/5qW2'

@app.route('/decode/<id>')
def decode(id):
    conn = getDbConnection()
    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]
        url_data = conn.execute('SELECT original_url FROM urls'
                                ' WHERE id = (?)', (original_id,)
                                ).fetchone()
        originalUrl = url_data['original_url']                                
        conn.commit()
        conn.close()
        return jsonify(
            originalUrl=originalUrl
        )
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))

# with app.test_client() as testClient:
#     response = testClient.get('/decode/5qW2')
#     jsonResponse = json.loads(response.get_data(as_text=True))
#     assert response.status_code == 200
#     assert jsonResponse['originalUrl'] == "https://en.wikipedia.org/wiki"
