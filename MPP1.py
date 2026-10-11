import pandas as pd                   # Traitement des données tabulaires
import numpy as np                    # Statistiques et calculs
import matplotlib.pyplot as plt       # Visualisation simple
import seaborn as sns                 # Visualisation avancée et heatmap
from datetime import datetime         # Manipulation de dates
import calendar                       # Noms des jours de la semaine
df = pd.read_csv("ecoute_musique.csv")
print(df.dtypes)
df["date"] = pd.to_datetime(df["date"])
df["heure_ecoute"] = pd.to_datetime(df["heure_ecoute"])
df["jour_semaine"] = df["date"].dt.day_name()
df["heure_arrondie"] = df["heure_ecoute"].dt.hour
df.duplicated()
df.duplicated().sum()
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
if "duree" in df.columns:
    df["duree"] = df["duree"].fillna(df["duree"].mean())
if "plateforme" in df.columns:
    df["plateforme"] = df["plateforme"].fillna("Inconnue")
if "genre" in df.columns:
    df["genre"] = df["genre"].fillna("Inconnu")
if "titre_morceau" in df.columns:
    df["titre_morceau"] = df["titre_morceau"].fillna("Titre inconnu")
df.isnull().sum()
ecoute_heure = df["heure_arrondie"].value_counts().sort_index()
print(ecoute_heure)

"""plt.plot(df["heure_arrondie"], df["heure_ecoute"])
plt.title("Repartition des écoutes par heure de la journée")
plt.xlabel("Heure")
plt.ylabel("Nombre d'écoute")"""

plt.figure(figsize=(5,5))
ecoute_heure.plot(kind="line", marker="o")
plt.title("Repartition des écoutes par heure de la journée")
plt.xlabel("Heure")
plt.ylabel("Nombre d'écoute")
plt.grid(True)
plt.show()

ecoute_jour = df["jour_semaine"].value_counts().sort_index()
print(ecoute_jour)

plt.figure(figsize=(5,5))
ecoute_jour.plot(kind="line", marker="o")
plt.title("Repartition des écoutes par jour de la semaine")
plt.xlabel("Jour")
plt.ylabel("Nombre d'écoute")
plt.show()

tableau = pd.crosstab(df["jour_semaine"], df["heure_arrondie"])
tableau = tableau.reindex(ecoute_jour)
plt.figure(figsize=(5,5))
sns.heatmap(tableau, annot=True, cmap="Blues")
plt.title("Heatmap des écoutes")
plt.xlabel("Heure")
plt.ylabel("Jour")
plt.show()

ecoute_genre = df["genre"].value_counts()
print(ecoute_genre)
print("Le genre le plus ecoutée est : ", ecoute_genre.idxmax())
print("\nGenre prefere par plateforme :")
genre_plateforme = pd.crosstab(df["plateforme"], df["genre"])
print(genre_plateforme)
print("\nLe genre le plus ecoute par plateforme est :")
print(genre_plateforme.idxmax(axis=1))

print("\nHeure la plus frequente pour chaque genre :")
genre_heure = pd.crosstab(df["genre"], df["heure_arrondie"])
print(genre_heure)
print("\nL'heure la plus frequente pour chaque genre est :")
print(genre_heure.idxmax(axis=1))

print("\nDuree moyenne d'ecoute selon les genres :")

duree_genre = df.groupby("genre")["duree"].mean()
print(duree_genre)

# Representation graphique
duree_genre.plot(kind="bar", color="orange")
plt.title("Duree moyenne d'ecoute selon les genres")
plt.xlabel("Genre musical")
plt.ylabel("Duree moyenne (minutes)")
plt.show()

