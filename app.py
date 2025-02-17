import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reviews = []

@app.route('/')
def index():
    return render_template('index.html', reviews=reviews)

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        book_title = request.form['title']
        book_review = request.form['review']
        reviews.append({'title': book_title, 'review': book_review})
        return redirect(url_for('index'))
    return render_template('review.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
