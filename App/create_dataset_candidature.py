
from models import Candidacy

def add_candidature():
    Candidacy(user_id = 5, entreprise = "facebook", contact_full_name = "Pierre S.", contact_email="admin@facebook.fb").save_to_db()
    Candidacy(user_id = 5, entreprise = "HP", contact_full_name = "Nick Johnson", contact_email="admin@hp.com").save_to_db()
    Candidacy(user_id = 6, entreprise = "ABC Company", contact_full_name = "Sabrina S.", contact_email="admin@abccompany.com").save_to_db()
    Candidacy(user_id = 6, entreprise = "Google", contact_full_name = "Sara I.", contact_email="admin@google.com").save_to_db()