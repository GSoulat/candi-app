from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,SubmitField,StringField
from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError,NumberRange
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
    contact_full_name = StringField(label='contact_full_name', validators=[DataRequired()])
    contact_email = StringField(label='contact_email', validators=[DataRequired()])
    contact_mobilephone = StringField(label='contact_mobilephone')
    status = StringField(label='Status', validators=[DataRequired()])

    submit = SubmitField(label="Valider")

class ModifyProfile(FlaskForm):
    """[Form to modify profile]
    """
    last_name = StringField(label="Nom", validators = [DataRequired(), Length(max=50)])
    first_name = StringField(label="Prénom", validators = [DataRequired(), Length(max=50)])
    email_address = EmailField(label="Adresse mail:", validators = [DataRequired()])
    telephone_number = StringField(label='Numéro de mobile :', validators=[Length(max=10)])   # street_number = StringField(label="Adresse mail:", validators = [DataRequired(), NumberRange(), Length(max=5)])
    submit = SubmitField(label="Valider")