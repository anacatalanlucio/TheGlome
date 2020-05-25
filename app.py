from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('Index.html')

@app.route('/Earth')
def Earth():
    return render_template('Earth.html')

@app.route('/Books')
def Books():
    return render_template('Books.html')

@app.route('/PowerNow')
def PowerNow():
    return render_template('PowerNow.html')

@app.route('/Collection')
def Collection():
    return render_template('Collection.html')

@app.route('/Mind')
def Mind():
    return render_template('Mind.html')

@app.route('/Movies')
def Movies():
    return render_template('Movies.html')

@app.route('/HighSociety')
def HighSociety():
    return render_template('HighSociety.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Starlink')
def Starlink():
    return render_template('Starlink.html')

@app.route('/BucketList')
def BucketList():
    return render_template('BucketList.html')

if __name__ == '__main__':
    app.run(debug = True)
