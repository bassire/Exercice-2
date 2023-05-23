class Personne:
    def __init__(info, nom, age):
        info.nom = nom
        info.age = age
    
    def afficher_informations(info):
        print("Nom:", info.nom)
        print("Âge:", info.age)


personne1 = Personne("Naruto", 23)
personne1.afficher_informations()