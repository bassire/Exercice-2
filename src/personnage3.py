class Personnage3:
    def __init__(self, nom, age, sexe, inventaire, force, agilite, endurance, arme, armure, compétences):
        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.force = force
        self.agilite = agilite
        self.endurance = endurance
        self.inventaire = inventaire
        self.arme = arme
        self.armure = armure
        self.compétences = compétences
    
    def attaquer(self):
        print("Le personnage 3 attaque.")
    
    def seDeplacer(self):
        print("Le personnage 3 se déplace.")
    
    def parler(self):
        print("Le personnage 3 parle.")
    
    def utiliserObjet(self):
        print("Le personnage 3 utilise un objet.")