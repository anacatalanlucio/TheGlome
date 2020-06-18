from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/earth')
def earth():
    return render_template('earth.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/powernow')
def PowerNow():
    return render_template('powernow.html')

@app.route('/collection')
def collection():
    return render_template('collection.html')

@app.route('/mind')
def mind():
    return render_template('mind.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/highsociety')
def highsociety():
    return render_template('highsociety.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/starlink')
def starlink():
    return render_template('starlink.html')

@app.route('/bucketlist')
def bucketlist():
    return render_template('buckelist.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
