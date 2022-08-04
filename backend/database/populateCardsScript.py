import pandas as pd

from databasehelper import * 

data = pd.read_csv('backend/database/PopulateCardsTableData/allValues.csv')
allCards = []
empty_cards_table()
#Note this data is still not full, but good enough for testing
for x in data.iterrows():
    create_card(x[1]["NAME"], x[1]["SCORE"],1,1,1,"someLink")