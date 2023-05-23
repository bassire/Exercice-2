class Personnage1:
    def __init__(self, nom, age, sexe, force, agilite, endurance, inventaire, arme, armure, compétences):
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
        print("Le personnage 1 attaque.")
    
    def seDeplacer(self):
        print("Le personnage 1 se déplace.")
    
    def parler(self):
        print("Le personnage 1 parle.")
    
    def utiliserObjet(self):
        print("Le personnage 1 utilise un objet.")
