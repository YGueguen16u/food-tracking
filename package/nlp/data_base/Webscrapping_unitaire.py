import pandas as pd
from bs4 import BeautifulSoup
import os

# Lire le fichier HTML
with open('html_webscrap_one.txt', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# Extraire les données du fichier HTML
data = {}
for div in soup.find_all('div', class_='d-flex nutrition-row position-relative'):
    nutrient = div.find('div', class_='font-subtitle light mt-0').text.strip()
    value = div.find('span', class_='serving-calculator-table-value').text.strip()
    unit = div.find('div').text.strip().split('\n')
    if len(unit) > 1:
        unit = unit[1].strip()
    else:
        unit = ''
    data[nutrient] = {'value': value, 'unit': unit}

# Lire le fichier CSV existant
df = pd.read_csv('aliments.csv', encoding='ISO-8859-1')

# Déterminer le nouvel ID
if os.stat('aliments.csv').st_size == 0:
    new_id = 1
else:
    new_id = df['id'].max() + 1

# Ajouter les nouvelles données au DataFrame
new_row = {'id': new_id, 'Aliment': 'Nouvel Aliment'}
for nutrient, info in data.items():
    new_row[nutrient] = info['value']
    new_row[nutrient + '_unit'] = info['unit']
df = df.append(new_row, ignore_index=True)

# Écrire dans le fichier CSV
df.to_csv('aliments.csv', index=False)
