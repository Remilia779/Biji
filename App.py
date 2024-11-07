from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    Nick = "Rozalan"
    ID = "289214378"
    return render_template('about.html', Nick=Nick, ID=ID)

if __name__ == '__main__':
    app.run(debug=True)
