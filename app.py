from flask import Flask, render_template
#inizializza l'app Flask
app = Flask(__name__)

lista_spesa = ["Pesca", "Mele", "Carne"]
#rotta principale
@app.route('/')
def home():
    return render_template('index.html', lista = lista_spesa)
#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)