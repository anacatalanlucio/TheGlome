from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/atelier')
def atelier():
    return render_template('atelier.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/powernow')
def PowerNow():
    return render_template('powernow.html')

@app.route('/collection')
def collection():
    return render_template('collection.html')

@app.route('/diaries')
def diaries():
    return render_template('diaries.html')

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


@app.route('/womanplan')
def womanplan():
    return render_template('womanplan.html')

@app.route('/solteras')
def solteras():
    return render_template('solteras.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
