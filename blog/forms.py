from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField, EmailField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from blog.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', 
      validators=[DataRequired("Campo Obbligatorio")])
    password = PasswordField('Password', 
      validators=[DataRequired("Campo Obbligatorio")])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Titolo', 
      validators = [DataRequired("Campo Obbligatorio"), Length(min=3, max=120, message="Assicurati che il titolo abbia tra i 3 ed i 120 caratteri")])
    description = TextAreaField('Descrizione', 
      validators=[Length(max=240, message="Assicurati che la descrizione non superi i 240 caratteri")])
    body = TextAreaField('Contenuto', 
      validators=[DataRequired("Campo Obbligatorio")])
    image = FileField('Copertina Articolo', 
        validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Pubblica Post')

class SignupForm(FlaskForm):
    username = StringField('Username',
      validators=[DataRequired("Campo Obligatorio"), Length(8, 64),
                  Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password',
      validators=[DataRequired("Campo Obbligatorio"), EqualTo ('confirmpassword', message='Passwords must match.')])
    confirmpassword = PasswordField('Conferma Password', 
      validators=[DataRequired("Campo Obbligatorio")])
    email = EmailField('Email', validators=[DataRequired("Campo Obbligatorio"), Length(1, 64), Email()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
 
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
  #Il validator usato nel campo “username”, si assicura che vengano utilizzati solo
  #lettere, numeri, punti e underscores altrimenti ritorna il messaggio di errore,
  #passato come argomento a Regexp.
  #Nel campo password abbiamo un altro validator (EqualTo) che si assicura che le
  #password immesse (password e conferma della stessa) siano uguali.
  #I due metodi validate_email() e validate_username() si assicurano che i valori
  #immessi nei campi non siano già presenti a database, sollevando in caso affermativo,
  #l’eccezione di competenza.    