import pandas as pd
import math
from databasehelper import * 

data = pd.read_csv('database/PopulateCardsTableData/allValues.csv')
allCards = []
empty_cards_table()
#Note this data is still not full, but good enough for testing
for x in data.iterrows():
    if math.isnan(x[1]["SCORE"]):
        create_card(x[1]["NAME"],99,1,1,1,"someLink")
    else:
        create_card(x[1]["NAME"], x[1]["SCORE"],1,1,1,"someLink")
print("Cards added")