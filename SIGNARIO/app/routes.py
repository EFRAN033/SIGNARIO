from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Camara.html')  # Página que se muestra en "/"

@app.route('/camara')
def camara():
    return render_template('Camara.html')  # Página específica para "/camara"

@app.route('/nosotros')
def nosotros():
    return render_template('Nosotros.html') # Pagina especifica para "/nosotros"

@app.route('/biblioteca')
def biblioteca():
    return render_template('Biblioteca.html') # Pagina especfica para "/biblioteca"


if __name__ == '__main__':
    app.run(debug=True)
