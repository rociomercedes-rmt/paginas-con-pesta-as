from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/orientaciones')
def orientaciones(): # <-- Coincide con url_for('orientaciones')
    return render_template('orientaciones.html')

@app.route('/historia')
def historia(): # <-- Coincide con url_for('historia')
    return render_template('historia.html')


@app.route('/inscripcion')
def inscripcion(): # <-- Coincide con url_for('inscripcion')
    return render_template('inscripcion.html')

if __name__ == '__main__':
    app.run(debug=True)