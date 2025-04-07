##TD-TP2
##EXERCICE1
# 1. Définir une liste Semaine avec les jours de la semaine et l'afficher
Semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
print("Liste des jours de la semaine :", Semaine)

# 2. Remplir la liste Couleurs avec 5 couleurs différentes et l'afficher
Couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Noir"]
print("Liste des couleurs :", Couleurs)

# 3. Définir une liste de 7 réels et afficher les éléments aux indices 1, 3 et 5
Reels = [3.5, 7.2, 1.0, 8.4, 2.9, 6.1, 4.3]
print("Élément à l'indice 1 :", Reels[1])
print("Élément à l'indice 3 :", Reels[3])
print("Élément à l'indice 5 :", Reels[5])

##EXERCICE2
# 1
mylist = ['apple', 'banana', 'cherry'] 
print(mylist[1])  # Résultat : banana

# 2
mylist = ['apple', 'banana', 'banana', 'cherry']  
print(mylist[2])  # Résultat : banana

# 3
thislist = ['apple', 'banana', 'cherry'] 
print(len(thislist))  # Résultat : 3 (taille de la liste)

# 4
mylist = ['apple', 'banana', 'cherry']  
print(mylist[-1])  # Résultat : cherry (dernier élément)

# 5
fruits = ["apple", "banana", "cherry"]  
print(fruits[1])  # Résultat : banana (2e élément)

# 6
mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']  
print(mylist[1:4])  # Résultat : ['banana', 'cherry', 'orange']

# 7 - Exercice 3
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  
print(fruits[2:5])  # Résultat : ['cherry', 'orange', 'kiwi']

##EXERCICE3
# Q1. Créer une liste de matières et l’afficher
matieres = ["Anglais", "Physique", "Maths", "Svt"]
print("1. Liste des matières :", matieres)

# Q2. Ajouter "Histoire" et "Geographie" à la liste
matieres.append("Histoire")
matieres.append("Geographie")
print("2. Liste mise à jour avec Histoire et Geographie :", matieres)

# Afficher les 4 premiers éléments
print("Les 4 premiers éléments :", matieres[:4])

# Afficher les 3 derniers éléments
print("Les 3 derniers éléments :", matieres[-3:])

# Afficher 3 éléments depuis le second indice
print("3 éléments depuis l’indice 2 :", matieres[2:5])


##EXERCICE4
# 1. Modifier le premier élément, afficher le deuxième
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print("1. Élément à l'indice 1 :", mylist[1])  

# 2. Modifier 'apple' en 'kiwi'
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print("2. Liste après modification :", fruits)  

# 3. Remplacer un élément par deux éléments
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print("3. Élément à l'indice 2 :", mylist[2])  

# 4. Insérer 'orange' au début de la liste et afficher le 2e élément
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print("4. Élément à l'indice 1 :", mylist[1])  

# 5. Ajouter 'orange' à la fin de la liste avec append()
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("5. Liste après append :", fruits)  

# 6. Insérer 'lemon' à la 2e position avec insert()
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print("6. Liste après insertion de 'lemon' :", fruits)  


##EXERCICE5
# 1. Utilisation de la méthode 'remove' pour supprimer la valeur 'mer' de la liste
Semaine = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim']
Semaine.remove('mer')
print("Liste après suppression de 'mer' :", Semaine)

# 2. Utilisation de la méthode 'pop' pour supprimer l'élément à l'index 1 de la liste
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print("Liste après pop à l'index 1 :", mylist)

# 3. Utilisation de la méthode 'clear' pour vider la liste
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print("Liste après utilisation de 'clear' :", fruits)
