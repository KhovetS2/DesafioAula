from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contatos')
def contatos():
    return render_template("contatos.html")

@app.route('/quem-somos')
def quem_somos():
    return render_template("quem-somos.html")

@app.route('/tecnoblog')
def tecnoblog():
    return render_template('tecnoblog.html')


if __name__ == "__main__":
    app.run(debug=True)