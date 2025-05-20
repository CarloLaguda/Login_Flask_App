import pymysql

class DatabaseWrapper:
    
    #costruttore ogg db
    def __init__(self, host, port, password, user, database):
        self.db_config = {
            'host': host,
            'user': user,
            'port': port,
            'password': password,
            'database': database,
            'cursorclass': pymysql.cursors.DictCursor  #restituisce i risultati come dizionario
        }
        self.create_table()  #creazione della tabella all'avvio

    #connessione al db
    def connect(self):
        return pymysql.connect(**self.db_config)

    #fa le operazioni di DML e DDL
    def execute_query(self, query, params=()):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
        conn.close()

    #per eseguire le select (fa le operazioni di DQL)
    def fetch_query(self, query, params=()):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        conn.close()
        return result #restituisce il risultato delle select

    #creo tabella con execute_query!!!!
    def create_table(self):
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS ListaSpesa (
                id INT AUTO_INCREMENT PRIMARY KEY,
                elemento VARCHAR(100) NOT NULL
            )
        ''')

    #le SELECT con con fetch_query!!!!
    def get_lista_spesa(self):
        return self.fetch_query('SELECT * FROM ListaSpesa')

    #manipolazione tabelle con execute_query!!!!
    def aggiungi_elemento(self, elemento):
        self.execute_query('INSERT INTO ListaSpesa (elemento) VALUES (%s)', (elemento,))
        
    #%s fa da placeholder: "la variabile che passo come parametro prende il valore di %s"

    def rimuovi_elemento(self, indice):
        self.execute_query('DELETE FROM ListaSpesa WHERE id = %s', (indice,))

    def svuota_lista(self):
        self.execute_query('DELETE FROM ListaSpesa')