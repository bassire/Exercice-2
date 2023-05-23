from personnage1 import Personnage1
from personnage2 import Personnage2
from personnage3 import Personnage3

if __name__ == "__main__":
    inventaire1 = ['épée', 'armure']
    compétences1 = ['force surhumaine', 'agilité accrue']
    personnage1 = Personnage1("Tauriel", 25, "Femme", 10, 5, 8, inventaire1, "arc", "armure", compétences1)

    inventaire2 = ['arc', 'flèches']
    compétences2 = ['tir précis', 'camouflage']
    personnage2 = Personnage2("Arthur", 30, "Homme", 8, 7, 6, inventaire2, "épée", "armure légère", compétences2)

    inventaire3 = ['baguette magique', 'potion']
    compétences3 = ['sorts puissants', 'guérison']
    personnage3 = Personnage3("Davy Jones", 87, "Homme", 6, 9, 4, inventaire3, "Sabre", "armure magique", compétences3)

    print("Les caracteristique du Personnage 1")
    print("Nom:", personnage1.nom)
    print("Âge:", personnage1.age)
    print("Sexe:", personnage1.sexe)
    print("Force:", personnage1.force)
    print("Agilité:", personnage1.agilite)
    print("Endurance:", personnage1.endurance)
    print("Inventaire:", personnage1.inventaire)
    print("Arme:", personnage1.arme)
    print("Armure:", personnage1.armure)
    print("Compétences:", personnage1.compétences)

    print("Les caracteristique du Personnage 2")
    print("Nom:", personnage2.nom)
    print("Âge:", personnage2.age)
    print("Sexe:", personnage2.sexe)
    print("Force:", personnage2.force)
    print("Agilité:", personnage2.agilite)
    print("Endurance:", personnage2.endurance)
    print("Inventaire:", personnage2.inventaire)
    print("Arme:", personnage2.arme)
    print("Armure:", personnage2.armure)
    print("Compétences:", personnage2.compétences)

    print("Les caracteristique du Personnage 3")
    print("Nom:", personnage3.nom)
    print("Âge:", personnage3.age)
    print("Sexe:", personnage3.sexe)
    print("Force:", personnage3.force)
    print("Agilité:", personnage3.agilite)
    print("Endurance:", personnage3.endurance)
    print("Inventaire:", personnage3.inventaire)
    print("Arme:", personnage3.arme)
    print("Armure:", personnage3.armure)
    print("Compétences:", personnage3.compétences)

