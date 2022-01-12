import sqlite3
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os


def getDbConnection():
    connection = sqlite3.connect('urlShortener.db')
    connection.row_factory = sqlite3.Row
    return connection

SECRET_KEY = os.getenv('FLASK_SECRET', '0000')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

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
            shortdUrl=shortUrl
        )
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))

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
