##TD-TP4
##EXERCICE1
# Fonction pour afficher le menu et obtenir le choix de l'utilisateur
def afficher_menu():
    print("\nMenu:")
    print("1. Ajouter une personne")
    print("2. Rechercher une personne")
    print("3. Supprimer une personne")
    print("4. Quitter")
    return input("Choisissez une option (1/2/3/4) : ")

# 1. Création d'un dictionnaire pour stocker les informations
personnes = {}

# Boucle pour continuer à exécuter le programme jusqu'à ce que l'utilisateur choisisse de quitter
while True:
    choix = afficher_menu()

    if choix == '1':  # Ajouter une personne
        nom = input("Entrez le nom de la personne : ")
        age = input(f"Entrez l'âge de {nom} : ")

        if age.isdigit():  # Vérifie si l'âge est un nombre
            personnes[nom] = int(age)
            print(f"{nom} a été ajouté avec succès.")
        else:
            print("Veuillez entrer un âge valide.")

    elif choix == '2':  # Rechercher une personne
        nom = input("Entrez le nom de la personne à rechercher : ")
        if nom in personnes:
            print(f"{nom} a {personnes[nom]} ans.")
        else:
            print(f"{nom} n'est pas dans le dictionnaire.")

    elif choix == '3':  # Supprimer une personne
        nom = input("Entrez le nom de la personne à supprimer : ")
        if nom in personnes:
            del personnes[nom]
            print(f"{nom} a été supprimé du dictionnaire.")
        else:
            print(f"{nom} n'est pas dans le dictionnaire.")

    elif choix == '4':  # Quitter
        print("Au revoir!")
        break

    else:
        print("Option invalide, veuillez réessayer.")

##EXERCICE2 
# Fonction pour fusionner deux dictionnaires
def fusionner_dictionnaires(d1, d2):
    # Fusionner les deux dictionnaires
    d3 = d1.copy()  # Copier d1 pour éviter de modifier l'original
    
    for key, value in d2.items():
        if key in d3:
            if isinstance(d3[key], (int, float)) and isinstance(value, (int, float)):
                d3[key] += value  # Ajouter si les deux valeurs sont numériques
            elif isinstance(d3[key], str) and isinstance(value, str):
                d3[key] += value  # Concaténer si les deux valeurs sont des chaînes
        else:
            d3[key] = value  # Ajouter la clé et sa valeur si elle n'existe pas dans d3

    # Retourner le dictionnaire trié par ordre alphabétique des clés
    return dict(sorted(d3.items()))

# Exemple d'utilisation
d1 = {"a": 10, "b": "test"}
d2 = {"a": 5, "c": "data"}

# Fusionner les dictionnaires
resultat = fusionner_dictionnaires(d1, d2)

# Affichage du résultat
print(resultat)


##EXERCICE3
# 1. Créer un fichier texte avec des noms et des âges
def creer_fichier():
    with open("noms_ages.txt", "w") as f:
        f.write("Zakaria,22\n")
        f.write("Mohamed,24\n")
        f.write("Hamza,20\n")
        

# 2. Lire le fichier et stocker les données dans un dictionnaire
def lire_fichier():
    personnes = {}
    try:
        with open("noms_ages.txt", "r") as f:
            for ligne in f:
                nom, age = ligne.strip().split(',')
                personnes[nom] = int(age)
    except FileNotFoundError:
        print("Le fichier n'existe pas encore.")
    return personnes

# 3. Ajouter ou modifier un enregistrement
def ajouter_ou_modifier_enregistrement(personnes):
    nom = input("Entrez le nom à ajouter ou modifier : ")
    age = input(f"Entrez l'âge de {nom} : ")
    
    if age.isdigit():
        personnes[nom] = int(age)
        # Mettre à jour le fichier
        with open("noms_ages.txt", "w") as f:
            for nom, age in personnes.items():
                f.write(f"{nom},{age}\n")
        print(f"L'enregistrement pour {nom} a été ajouté/modifié avec succès.")
    else:
        print("Veuillez entrer un âge valide.")

# Programme principal
def menu():
    creer_fichier()  # Créer le fichier au départ (si besoin)
    
    personnes = lire_fichier()  # Lire le fichier et stocker dans un dictionnaire
    print("Dictionnaire des personnes :", personnes)
    
    while True:
        print("\nMenu :")
        print("1. Ajouter ou modifier un enregistrement")
        print("2. Quitter")
        choix = input("Choisissez une option (1/2) : ")
        
        if choix == '1':
            ajouter_ou_modifier_enregistrement(personnes)
        elif choix == '2':
            print("Au revoir!")
            break
        else:
            print("Option invalide, réessayez.")

# Lancer le programme
menu()


##EXERCICE4
# 1. Créer un fichier texte avec des noms et des notes
def creer_fichier():
    with open("notes_etudiants.txt", "w") as f:
        f.write("Hamza,10\n")
        f.write("Ziko,20\n")
        f.write("Med,18\n")
        f.write("jamila,12\n")

# 2. Lire le fichier et stocker les données dans un dictionnaire
def lire_fichier():
    etudiants = {}
    try:
        with open("notes_etudiants.txt", "r") as f:
            for ligne in f:
                nom, note = ligne.strip().split(',')
                etudiants[nom] = float(note)
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    return etudiants

# 3. Calculer la moyenne des notes
def calculer_moyenne(etudiants):
    total = sum(etudiants.values())
    moyenne = total / len(etudiants) if etudiants else 0
    return moyenne

# 4. Afficher les étudiants ayant une note supérieure à la moyenne
def afficher_etudiants_sup_moyenne(etudiants, moyenne):
    print(f"Note moyenne des étudiants : {moyenne:.2f}")
    print("\nÉtudiants ayant une note supérieure à la moyenne :")
    for nom, note in etudiants.items():
        if note > moyenne:
            print(f"{nom}: {note}")

# Programme principal
def menu():
    creer_fichier() 
    
    etudiants = lire_fichier()  
    moyenne = calculer_moyenne(etudiants)  
    
    afficher_etudiants_sup_moyenne(etudiants, moyenne)  
# Lancer le programme
menu()

##EXERCICE5
# 1. Définir la classe Etudiant avec les attributs nom, âge et note
class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    # 2. Implémenter la méthode afficher_info() pour afficher les informations de l'étudiant
    def afficher_info(self):
        print(f"Nom: {self.nom}, Âge: {self.age}, Note: {self.note}")
    
    # 3. Méthode statique pour calculer la moyenne des notes
    @staticmethod
    def calculer_moyenne(etudiants):
        if len(etudiants) == 0:
            return 0
        total_notes = sum(etudiant.note for etudiant in etudiants)
        return total_notes / len(etudiants)

# Création d'objets Etudiant
etudiant2 = Etudiant("Zakaria", 22, 12)
etudiant1 = Etudiant("Hamza", 20, 15)
etudiant3 = Etudiant("Mohamed", 21, 18)

# Afficher les informations des étudiants
etudiant1.afficher_info()
etudiant2.afficher_info()
etudiant3.afficher_info()

# Liste d'étudiants
etudiants = [etudiant1, etudiant2, etudiant3]

# Calculer la moyenne des notes
moyenne = Etudiant.calculer_moyenne(etudiants)
print(f"\nLa moyenne des notes est : {moyenne:.2f}")


##EXERCICE6
class CarnetAdresses:
    def __init__(self):
        self.contacts = {}

    def ajouter(self, nom, email, tele):
        self.contacts[nom] = {"email": email, "tele": tele}

    def rechercher(self, nom):
        if nom in self.contacts:
            return self.contacts[nom]
        else:
            return False

    def supprimer(self, nom):
        if nom in self.contacts:
            del self.contacts[nom]
        else:
            return False

    def afficher(self):
        for nom, infos in self.contacts.items():
            print(f"{nom} : {infos}")

    def enregistrer_fichier(self, nom_fichier):
        with open(nom_fichier, "w", newline="") as file:
            for nom, infos in self.contacts.items():
                file.write(f"{nom}, {infos['email']}, {infos['tele']}\n")


# --- Exemple d'utilisation ---
carnet = CarnetAdresses()
carnet.ajouter("samir", "samir@example.com", "0612345678")
print(carnet.rechercher("samir"))   # Affiche les infos
carnet.supprimer("samir")
print(carnet.rechercher("samir"))   # Affiche False

# Ajouter d'autres contacts
carnet.ajouter("amine", "amine@example.com", "0699999999")
carnet.ajouter("sara", "sara@example.com", "0677777777")

# Afficher tous les contacts
carnet.afficher()

# Sauvegarder dans un fichier texte
carnet.enregistrer_fichier("contacts.txt")


##EXERCICE7
# Définition de la classe Livre
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.statut = "disponible"  # Le livre est disponible par défaut

    def __str__(self):
        return f"{self.titre} de {self.auteur} - Statut: {self.statut}"

# Définition de la classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.livres = []  # Liste des livres dans la bibliothèque

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.statut == "disponible":
                livre.statut = "emprunté"
                print(f"Le livre '{titre}' a été emprunté.")
                return
        print(f"Le livre '{titre}' est soit introuvable, soit déjà emprunté.")

    def rendre_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.statut == "emprunté":
                livre.statut = "disponible"
                print(f"Le livre '{titre}' a été rendu.")
                return
        print(f"Le livre '{titre}' n'est pas emprunté ou introuvable.")

    def lister_livres_disponibles(self):
        livres_disponibles = [livre for livre in self.livres if livre.statut == "disponible"]
        if livres_disponibles:
            print("Livres disponibles :")
            for livre in livres_disponibles:
                print(f"- {livre}")
        else:
            print("Aucun livre disponible.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création de livres
    livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    livre2 = Livre("1984", "George Orwell")
    livre3 = Livre("Les Misérables", "Victor Hugo")
    
    # Création de la bibliothèque
    bibliotheque = Bibliotheque()
    
    # Ajouter des livres à la bibliothèque
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)
    bibliotheque.ajouter_livre(livre3)
    
    # Lister les livres disponibles
    bibliotheque.lister_livres_disponibles()
    
    # Emprunter un livre
    bibliotheque.emprunter_livre("1984")
    
    # Lister les livres disponibles après emprunt
    bibliotheque.lister_livres_disponibles()
    
    # Rendre un livre
    bibliotheque.rendre_livre("1984")
    
    # Lister les livres disponibles après retour
    bibliotheque.lister_livres_disponibles()

