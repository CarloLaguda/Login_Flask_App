from flask import Flask, render_template, request, redirect, url_for
from models import DatabaseWrapper


app = Flask(__name__)
#connessione al database metti i tuoi dati o:
db = DatabaseWrapper(
    host = "mysql-2866f0dc-iisgalvanimi-94a0.i.aivencloud.com",
    port = 27960,
    password = "AVNS_Gw45d55L_UtOUeZ0JSN",  
    user = "avnadmin",
    database = "lista_spesa"
)

@app.route('/')
def home():
    lista_spesa = db.get_lista_spesa()  #richiamo metodo fatto nella classe wrapper
    return render_template('index.html', lista=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        db.aggiungi_elemento(elemento)  #richiamo metodo fatto nella classe wrapper
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    db.rimuovi_elemento(indice)  #richiamo metodo fatto nella classe wrapper
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    db.svuota_lista()  #richiamo metodo fatto nella classe wrapper
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)