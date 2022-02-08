from logging import PlaceHolder
from flask_wtf import FlaskForm

from wtforms import PasswordField,EmailField,SubmitField,StringField,TextAreaField, IntegerField
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

    ville_entreprise = StringField(label='Ville de l\'entreprise', validators=[DataRequired()])
    contact_full_name = StringField(label='Nom du contact', validators=[DataRequired()])
    contact_email = StringField(label='Email du contact', validators=[DataRequired()])
    contact_mobilephone = StringField(label='Téléphone du contact')
    status = SelectField(label='Statut',choices=['En cours','Rejeté','Accepté','C\'est compliqué'], validators=[DataRequired()])
    date = DateField(label='Date de la candidature',validators=[DataRequired()],format='%Y-%m-%d')
    print("En cours d'ajout")
    submit = SubmitField(label='Ajouter')
    
    


class ModifyPassword(FlaskForm):
    """[Form to modify password]

    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    current_password = PasswordField(label="Mot de passe actuel:", validators = [DataRequired()])
    new_password = PasswordField(label="Nouveau mot de passe:", validators = [DataRequired()])
    
    submit = SubmitField(label="Valider")

class ModifyCandidacy(FlaskForm):
    """[form to modify candidacy]
    """

    entreprise = StringField(label='Entreprise', validators=[DataRequired()])
    ville_entreprise = StringField(label='Ville de l\'entreprise', validators=[DataRequired()])
    contact_full_name = StringField(label='Nom du contact', validators=[DataRequired()])
    contact_email = StringField(label='Email du contact', validators=[DataRequired()])
    contact_mobilephone = StringField(label='Téléphone du contact')
    status = SelectField(label='Statut',choices=['En cours','Rejeté','Accepté','C\'est compliqué'], validators=[DataRequired()])
    comment = TextAreaField(label='Commentaire')
    date = DateField(label='Date de la candidature',validators=[DataRequired()],format='%Y-%m-%d')

    submit = SubmitField(label="Valider")

class ModifyProfile(FlaskForm):
    """[Form to modify profile]
    """
    last_name = StringField(label="Nom", validators = [DataRequired(), Length(max=50)])
    first_name = StringField(label="Prénom", validators = [DataRequired(), Length(max=50)])
    email_address = EmailField(label="Adresse mail:", validators = [DataRequired()])
    telephone_number = StringField(label="Numéro de mobile :", validators=[Length(max=10)])   
    street_number = IntegerField(label="Numéro de rue", validators=[Length(max=5)])
    submit = SubmitField(label="Valider")