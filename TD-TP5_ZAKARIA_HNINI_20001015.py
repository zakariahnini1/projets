##TD-TP5
##EXERCICE1
import numpy as np

# 1. Création des tableaux

# Tableau 1D de 0 à 9
tableau_1D = np.arange(10)
print("Tableau 1D :", tableau_1D)

# Tableau 2D (3x3) avec des nombres aléatoires entre 0 et 1
tableau_2D = np.random.rand(3, 3)
print("\nTableau 2D :\n", tableau_2D)

# Tableau 3D (2x3x4) rempli de zéros
tableau_3D = np.zeros((2, 3, 4))
print("\nTableau 3D :\n", tableau_3D)

# 2. Accès et modification des éléments

# Troisième élément du tableau 1D (index 2 car les indices commencent à 0)
print("\nTroisième élément du tableau 1D :", tableau_1D[2])

# Deuxième ligne (index 1), première colonne (index 0) du tableau 2D
print("Élément [1][0] du tableau 2D :", tableau_2D[1, 0])

# Modification d'un élément du tableau 3D
tableau_3D[0, 1, 2] = 7
print("\nTableau 3D après modification :\n", tableau_3D)


##EXERCICE2
import numpy as np

# 1. Opérations élément par élément
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b

print("Addition :", addition)
print("Soustraction :", soustraction)
print("Multiplication :", multiplication)
print("Division :", division)

# 2. Fonctions mathématiques sur un tableau de 0 à π
valeurs = np.linspace(0, np.pi, 5)  # 5 valeurs de 0 à π

sinus = np.sin(valeurs)
cosinus = np.cos(valeurs)
exponentielle = np.exp(valeurs)

print("\nValeurs de 0 à π :", valeurs)
print("sin :", sinus)
print("cos :", cosinus)
print("exp :", exponentielle)

# 3. Sélection et remplacement dans un tableau d'entiers
tableau = np.arange(10)  # tableau d'entiers de 0 à 9
pairs = tableau[tableau % 2 == 0]  # sélection des éléments pairs

print("\nTableau original :", tableau)
print("Éléments pairs :", pairs)

# Remplacement des éléments impairs par -1
tableau_modifie = tableau.copy()
tableau_modifie[tableau_modifie % 2 != 0] = -1

print("Tableau après remplacement des impairs par -1 :", tableau_modifie)


##EXERCICE3
import numpy as np

# 1. Création d'un tableau 1D de 12 éléments
tableau = np.arange(12)
print("Tableau 1D :", tableau)

# Transformation en tableau 2D de dimensions (3, 4)
tableau_2D = tableau.reshape(3, 4)
print("\nTableau 2D (3x4) :\n", tableau_2D)

# Transformation en tableau 3D de dimensions (2, 2, 3)
tableau_3D = tableau.reshape(2, 2, 3)
print("\nTableau 3D (2x2x3) :\n", tableau_3D)

# 2. Transposer le tableau 2D (3x4 devient 4x3)
transpose = tableau_2D.T
print("\nTransposé du tableau 2D :\n", transpose)

# Utilisation de swapaxes
swap = np.swapaxes(tableau_2D, 0, 1)
print("\nSwapaxes (0 <-> 1) sur le tableau 2D :\n", swap)

# 3. Création de deux tableaux 2D (2x3)
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print("\nTableau a :\n", a)
print("Tableau b :\n", b)

# Concaténation verticale (résultat : 4x3)
concat_vert = np.vstack((a, b))
print("\nConcaténation verticale :\n", concat_vert)

# Concaténation horizontale (résultat : 2x6)
concat_horiz = np.hstack((a, b))
print("\nConcaténation horizontale :\n", concat_horiz)

# Découpage du tableau concaténé verticalement en deux tableaux (2 lignes chacun)
subarrays = np.vsplit(concat_vert, 2)
print("\nSous-tableaux après vsplit :")
for i, sub in enumerate(subarrays):
    print(f"Sous-tableau {i+1}:\n{sub}")


##EXERCICE4
import numpy as np

# 1. Créer un tableau aléatoire (5x5)
tableau = np.random.rand(5, 5)
print("Tableau aléatoire (5x5) :\n", tableau)

# Moyenne par ligne et par colonne
moyenne_lignes = np.mean(tableau, axis=1)
moyenne_colonnes = np.mean(tableau, axis=0)

# Écart-type par ligne et par colonne
ecart_type_lignes = np.std(tableau, axis=1)
ecart_type_colonnes = np.std(tableau, axis=0)

# Minimum et maximum par ligne et par colonne
min_lignes = np.min(tableau, axis=1)
max_lignes = np.max(tableau, axis=1)
min_colonnes = np.min(tableau, axis=0)
max_colonnes = np.max(tableau, axis=0)

print("\nMoyenne par ligne :", moyenne_lignes)
print("Moyenne par colonne :", moyenne_colonnes)
print("Écart-type par ligne :", ecart_type_lignes)
print("Écart-type par colonne :", ecart_type_colonnes)
print("Minimum par ligne :", min_lignes)
print("Maximum par ligne :", max_lignes)
print("Minimum par colonne :", min_colonnes)
print("Maximum par colonne :", max_colonnes)

# 2. Trier un tableau aléatoire et trouver l'indice du max
tableau_aleatoire = np.random.rand(10)
print("\nTableau aléatoire 1D :", tableau_aleatoire)

# Tri croissant
tableau_trie = np.sort(tableau_aleatoire)
print("Tableau trié :", tableau_trie)

# Indice de l'élément maximum dans le tableau d'origine
indice_max = np.argmax(tableau_aleatoire)
print("Indice de l'élément max dans le tableau original :", indice_max)

# 3. Broadcasting : multiplication tableau 1D (4) avec tableau 2D (3x4)
vecteur = np.array([1, 2, 3, 4])
matrice = np.random.randint(1, 5, (3, 4))

print("\nTableau 1D :", vecteur)
print("Tableau 2D (3x4) :\n", matrice)

# Multiplication par broadcasting
resultat = matrice * vecteur
print("Résultat de la multiplication (broadcasting) :\n", resultat)
 

##EXERCICE5
import numpy as np

# Colonnes avec distributions différentes
col1 = np.random.uniform(-1, 1, 100)
col2 = np.random.exponential(1, 100)
col3 = np.random.binomial(10, 0.5, 100)

# Stack les colonnes
data = np.column_stack((col1, col2, col3))

# Matrice de covariance
cov_matrix = np.cov(data, rowvar=False)
print("Matrice de covariance :\n", cov_matrix)


from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

# Signal sinusoïdal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)

# FFT avec scipy
fft_result = fft(signal)
frequencies = fftfreq(len(t), d=t[1] - t[0])

# Affichage du spectre
plt.plot(frequencies[:500], np.abs(fft_result)[:500])
plt.title("Spectre via scipy.fft")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Lancers de dés avec matrice
des = np.random.randint(1, 7, (2, 1000))
somme = des.sum(axis=0)

# Histogramme avec np.histogram
hist, bins = np.histogram(somme, bins=np.arange(1.5, 13.5, 1))

# Affichage
plt.bar(bins[:-1], hist, width=0.9, edgecolor='black')
plt.title("Histogramme des sommes (numpy.histogram)")
plt.xlabel("Somme")
plt.ylabel("Nombre de cas")
plt.grid(True)
plt.show()


##EXERCICE6
import numpy as np

class AnalyseVentes:
    def __init__(self):
        self.produits = ['P1', 'P2', 'P3']
        self.mois = np.array(["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"])
        np.random.seed(1)
        self.ventes = np.random.randint(100, 1001, size=(12, 3))

    def afficher_tableau(self):
        print("=== VENTES MENSUELLES ===")
        print(self.ventes)

    def total_annuel_par_produit(self):
        totaux = self.ventes.sum(axis=0)
        print("\n=== TOTAL ANNUEL PAR PRODUIT ===")
        for i, produit in enumerate(self.produits):
            print(f"{produit} : {totaux[i]}")
        return totaux

    def moyenne_mensuelle_par_produit(self):
        moyennes = self.ventes.mean(axis=0)
        print("\n=== MOYENNE MENSUELLE PAR PRODUIT ===")
        for i, produit in enumerate(self.produits):
            print(f"{produit} : {moyennes[i]:.2f}")
        return moyennes

    def mois_ventes_max(self):
        indices = self.ventes.argmax(axis=0)
        print("\n=== MOIS AVEC VENTES MAXIMALES ===")
        for i in range(3):
            print(f"{self.produits[i]} : {self.mois[indices[i]]} ({self.ventes[indices[i], i]})")
        return indices

    def croissance_mensuelle(self):
        croissance = np.diff(self.ventes, axis=0) / self.ventes[:-1] * 100
        print("\n=== CROISSANCE MENSUELLE (%) ===")
        print(np.round(croissance, 2))
        return croissance

    def mois_plus_forte_croissance(self):
        croissance = self.croissance_mensuelle()
        indices = croissance.argmax(axis=0) + 1
        print("\n=== MOIS AVEC LA PLUS FORTE CROISSANCE ===")
        for i in range(3):
            mois = self.mois[indices[i]]
            valeur = croissance[indices[i]-1, i]
            print(f"{self.produits[i]} : {mois} (+{valeur:.2f}%)")
        return indices

    def ventes_totales_par_mois(self):
        totaux = self.ventes.sum(axis=1)
        print("\n=== VENTES TOTALES PAR MOIS ===")
        for i in range(12):
            print(f"{self.mois[i]} : {totaux[i]}")
        return totaux

# -----------------------------
# Utilisation de la classe
# -----------------------------
analyse = AnalyseVentes()
analyse.afficher_tableau()
analyse.total_annuel_par_produit()
analyse.moyenne_mensuelle_par_produit()
analyse.mois_ventes_max()
analyse.mois_plus_forte_croissance()
analyse.ventes_totales_par_mois()

