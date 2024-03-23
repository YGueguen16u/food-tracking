import pandas as pd 

# Définition des colonnes
colonnes = ['id', "Aliment", 'Valeur calorique', 'Lipides', 'Glucides', 'Protéine', 'Fibre alimentaire', 
            'Cholestérol', 'Sodium', 'Eau', 'Vitamine A', 'Vitamine B1', 'Vitamine B11', 'Vitamine B12', 
            'Vitamine B2', 'Vitamine B3', 'Vitamine B5', 'Vitamine B6', 'Vitamine C', 'Vitamine D', 
            'Vitamine E', 'Vitamine K', 'Calcium', 'Cuivre', 'Fer', 'Magnésium', 'Manganèse', 'Phosphore', 
            'Potassium', 'Sélénium', 'Zinc']

# Création d'un DataFrame vide avec les colonnes spécifiées
df_vide = pd.DataFrame(columns=colonnes)

# Sauvegarde du DataFrame vide dans un fichier CSV
chemin_fichier_csv = r"C:\Users\GUEGUEN\Desktop\WSApp\tracker_alimentaire\package\nlp\data_base\aliments_vide.csv"
df_vide.to_csv(chemin_fichier_csv, index=False)