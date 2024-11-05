from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    nama = "Bintang Sayidina Alansyah"
    npm = "5230411276"
    return render_template('about.html', nama=nama, npm=npm)

if __name__ == '__main__':
    app.run(debug=True)
