from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy #ci permettere di poter interrogare il database in con linguaggio python che verrà poi trasformato in sql
from flask_migrate import Migrate
from flask_misaka import Misaka
from config import Config

app = Flask(__name__) #inizializziamo la nostra app con flask 
app.config.from_object(Config) #integriamo il database nella nostra applicazione

Misaka(app)

db = SQLAlchemy(app) #passiamo la nostra istanza di flask alla nostra variabile
migrate = Migrate(app, db) #ci permette di effettuare modifiche alla struttura del database in maniera semplice
login_manager = LoginManager(app)

with app.app_context():
  if db.engine.url.drivername == 'sqlite':
    migrate.init_app(app, db, render_as_batch=True)
  else:
    migrate.init_app(app, db)
#stiamo aggiungendo questo parametro render_as_batch=True qual'ora la nostra applicazione stia utilizzando come dabase sqlite serve per venire incontro alle limitazioni
#di questo specifico dabase, se dobbiamo apportare delle modiche allo schema del database viene creato un clone della tabella più le modifiche

from blog import errors, models, routes
#una volta importato models con i modelli lanciamo il dabase da terminale con flask db init
# creiamo le tabelle con flask migrate - flask db migrate -m "Creazione Tabelle Post e User"
# andiamo ad apportare le modifiche tramite le nuove funzioni che sono state create flask db upgrade