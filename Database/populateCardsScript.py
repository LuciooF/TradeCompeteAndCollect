import pandas as pd

from databasehelper import CardRarity, create_card, empty_cards_table

data = pd.read_csv('Database/PopulateCardsTableScript/allValues.csv')
allCards = []
empty_cards_table()
for x in data.iterrows():
    create_card(x[1]["NAME"], x[1]["SCORE"],1,1,1,CardRarity.CORE.value,"someLink")