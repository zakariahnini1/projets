##TD-TP3
##EXERCICE1
# 1. Liste des nombres
nombres = [4, 8, 15, 16, 23, 42]

# 2. Fonction 'affListe' qui affiche chaque élément de la liste
def affListe(maListe):
    for element in maListe:
        print(element)
affListe(nombres)


##EXERCICE2
# 1. Fonction qui retourne la somme des éléments d'une liste
def somme_liste(liste):
    return sum(liste)

# 2. Fonction qui retourne la moyenne des éléments d'une liste
def moyenne_liste(liste):
    return sum(liste) / len(liste) if len(liste) > 0 else 0  # Eviter la division par 0

# Liste des nombres
nombres = [4, 8, 15, 16, 23, 42]

# Calcul et affichage de la somme et de la moyenne des éléments de la liste
somme = somme_liste(nombres)
moyenne = moyenne_liste(nombres)

print("Somme des éléments :", somme)
print("Moyenne des éléments :", moyenne)

##EXERCICE3 
# 1. Définir la fonction qui extrait les nombres pairs
def extraire_pairs(liste):
    pairs = []
    for nombre in liste:
        if nombre % 2 == 0:
            pairs.append(nombre)
    return pairs

# 2. Tester la fonction avec une liste de nombres
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 3. Afficher la liste des nombres pairs retournée
nombres_pairs = extraire_pairs(nombres)
print("Nombres pairs :", nombres_pairs)

##EXERCICE4
# 1. Fonction qui vérifie si un élément existe dans la liste
def element_existe(liste, element):
    return element in liste

# Liste des nombres
nombres = [4, 8, 15, 16, 23, 42]

# 2. Test de la fonction avec l'élément 15 et l'élément 50
test_1 = element_existe(nombres, 15)  # Test avec l'élément 15
test_2 = element_existe(nombres, 50)  # Test avec l'élément 50

# Affichage des résultats
print("L'élément 15 existe-t-il dans la liste ? :", test_1)
print("L'élément 50 existe-t-il dans la liste ? :", test_2)

##EXERCICE5 
def liste_carres(liste):
    return [x**2 for x in liste]

nombres = [1, 2, 3, 4, 5, 6]
carres = liste_carres(nombres)
print(carres)  # Résultat : [1, 4, 9, 16, 25, 36]

##EXERCICE6
# 1. Fonction qui retourne le minimum et le maximum d'une liste sous forme de tuple
def trouver_min_max(liste):
    return (min(liste), max(liste))

# Liste des nombres
nombres = [4, 8, 15, 16, 23, 42]

# 2. Test de la fonction avec la liste nombres
min_max = trouver_min_max(nombres)

# Affichage du minimum et du maximum retournés
print("Le minimum et le maximum de la liste sont :", min_max)
   

##EXERCICE7 
# 1. Créer les deux listes
nombres = [3, 8, 1, 15, 6]
autres_nombres = [7, 11, 19, 24, 33]

# 2. Fonction de fusion et tri
def fusionner_et_trier(liste1, liste2):
    return sorted(liste1 + liste2)

# 3. Test de la fonction
fusion = fusionner_et_trier(nombres, autres_nombres)
print("Fusion triée :", fusion)


##EXERCICE8
# 1. Fonction qui vérifie si un mot est un palindrome
def est_palindrome(mot):
    return mot == mot[::-1]

# 2. Test de la fonction avec les mots "radar", "python" et "level"
mots = ["radar", "python", "level"]
for mot in mots:
    print(f"Le mot '{mot}' est un palindrome ? {est_palindrome(mot)}")
