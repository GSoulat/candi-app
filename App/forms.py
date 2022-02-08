from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,SubmitField,StringField,TextAreaField
from wtforms.fields import DateField,SelectField

from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError
from .models import Users

class Login(FlaskForm):
    """[Form to login]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    password = PasswordField(label="Mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Se connecter")


class AddCandidacy(FlaskForm):
    """[Form to add candidacy]
    """
    entreprise = StringField(label='Entreprise', validators=[DataRequired()])
    contact_full_name = StringField(label='contact_full_name', validators=[DataRequired()])
    contact_email = StringField(label='contact_email', validators=[DataRequired()])
    contact_mobilephone = StringField(label='contact_mobilephone')
    status = SelectField(label='Status',choices=['En cours','Rejeté','Accepté','C\'est compliqué'], validators=[DataRequired()])
    date = DateField(label='Date de la candidature',validators=[DataRequired()],format='%Y-%m-%d')
    submit = SubmitField(label='Ajouter')

    

class ModifyProfile(FlaskForm):
    """[Form to modify profile]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    current_password = PasswordField(label="Mot de passe actuel:", validators = [DataRequired()])
    new_password = PasswordField(label="Nouveau mot de passe:", validators = [DataRequired()])
    
    submit = SubmitField(label="Valider")

class ModifyCandidacy(FlaskForm):
    """[form to modify candidacy]
    """
    contact_full_name = StringField(label='contact_full_name', validators=[DataRequired()])
    contact_email = StringField(label='contact_email', validators=[DataRequired()])
    contact_mobilephone = StringField(label='contact_mobilephone')
    status = SelectField(label='Status',choices=['En cours','Rejeté','Accepté','C\'est compliqué'], validators=[DataRequired()])
    comment = TextAreaField(label='Commentaire')
    date = DateField(label='Date de la candidature',validators=[DataRequired()],format='%Y-%m-%d')

    submit = SubmitField(label="Valider")