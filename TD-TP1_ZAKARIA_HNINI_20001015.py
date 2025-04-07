##TD-TP1 
##EXERCICE1
# Q1
# Affectation multiple
texte, entier, decimal = ("Bonjour", 21, 3.14)

# Affichage des types
print(type(texte))   # <class 'str'>
print(type(entier))  # <class 'int'>
print(type(decimal)) # <class 'float'>"""





# Q2
# Affectation multiple avec mes infos personnelles
nom, prenom, age = ("Hnini", "Zakaria", 22)

# Affichage des valeurs
print("Nom :", nom)
print("Prénom :", prenom)
print("Âge :", age)


##EXERCICE2
#Q1
# Saisie des notes
anglais = float(input("Note en Anglais : "))
physique = float(input("Note en Physique : "))
maths = float(input("Note en Maths : "))
svt = float(input("Note en SVT : "))

# Saisie des coefficients
coef_ang = int(input("Coefficient Anglais : "))
coef_phy = int(input("Coefficient Physique : "))
coef_math = int(input("Coefficient Maths : "))
coef_svt = int(input("Coefficient SVT : "))

# Calcul de la moyenne pondérée
somme_notes = (anglais * coef_ang + physique * coef_phy + maths * coef_math + svt * coef_svt)
somme_coefs = (coef_ang + coef_phy + coef_math + coef_svt)
moyenne = somme_notes / somme_coefs

print("La moyenne des notes est :", round(moyenne, 2))

#Q2
budget = float(input("Entrez votre budget : "))
achats = float(input("Montant des achats : "))

if budget >= achats:
    print(f"Vous pouvez payer les achats. Il vous restera {budget - achats:} DH.")
else:
    print(f"Le budget est insuffisant. Il vous manque {achats - budget:} DH.")



##EXERCICE3
import math  # Pour utiliser la constante math.pi

# Saisie des valeurs
rayon = float(input("Entrez le rayon du cône : "))
hauteur = float(input("Entrez la hauteur du cône : "))

# Calcul du volume
volume = (1/3) * math.pi * rayon**2 * hauteur
print("Le volume du cône est :", round(volume, 2), "unités cubes")



##EXERCICER4
import math  # pour utiliser math.pi

# Saisie des rayons
Rg = float(input("Entrez le rayon du grand disque (Rg) : "))
Rp = float(input("Entrez le rayon du trou central (Rp) : "))

# Vérification que Rp < Rg
if Rp >= Rg:
    print("Erreur : Le rayon du trou (Rp) doit être inférieur au rayon du disque (Rg).")
else:
    # Calcul de la surface utile
    surface = math.pi * (Rg**2 - Rp**2)
    print("La surface utile du disque découpé est :", round(surface, 2), "unités carrées.")



##EXERCICE5
# Saisie d'une phrase par l'utilisateur
phrase = input("Saisis une phrase : ")

# Calcul de la longueur
longueur = len(phrase)

# Vérification si la longueur est paire ou impaire
milieu = longueur // 2

if longueur % 2 == 0:
    print("La longueur est paire.")
    print("Première moitié :", phrase[:milieu])
else:
    print("La longueur est impaire.")
    print("Seconde moitié :", phrase[milieu:])
 
