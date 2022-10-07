from datetime import datetime
from django.db import connection
import mysql.connector
import os
from enum import Enum
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

db = mysql.connector.connect(
    host="localhost",
    user=os.getenv("DBUSER"),
    passwd = os.getenv("DBPASSWORD"),
    database=os.getenv("DBNAME")
)
cursor = db.cursor(buffered=True)

def create_user(username, discordId):
    cursor.execute("INSERT INTO user (username, discordid) VALUES (%s,%s)", (username,discordId))
    db.commit()
    createdUserId = cursor.lastrowid
    cursor.execute(f"SELECT * FROM user WHERE userId = {createdUserId}")
    return map_user(cursor)[0]
def create_card(veefriend, score, aura, skill,stamina, coreImageLink):
    cursor.execute("INSERT INTO card (veefriend, score, aura, skill, stamina, coreImageLink) VALUES (%s,%s,%s,%s,%s,%s)", (veefriend,score,aura,skill,stamina,coreImageLink))
    db.commit()
    createdCardId = cursor.lastrowid
    cursor.execute(f"SELECT * FROM card WHERE cardId = {createdCardId}")
    return map_cards(cursor)[0]
def add_card_to_user(userId, cardId):
    cursor.execute("INSERT INTO usercards (userId, cardId) VALUES (%s,%s)", (userId,cardId))
    db.commit()
def remove_card_from_user(userId, cardId):
    cursor.execute(f"DELETE FROM usercards WHERE userId={userId} AND cardId={cardId}")
    db.commit()
def remove_user(userId):
    cursor.execute(f"DELETE FROM user WHERE userId={userId}")
    db.commit()
def get_user(userId):
    cursor.execute(f"SELECT * FROM user WHERE userId={userId}")
    results = map_user(cursor)
    return results[0]
def get_user_by_discord_id(discordId):
    query = f"SELECT * FROM user WHERE discordId={discordId}"
    cursor.execute(query)
    allResults = map_user(cursor)
    return allResults[0]
def get_card(cardId):
    query = f"SELECT * FROM card WHERE cardId={cardId}"
    cursor.execute(query)
    return map_cards(cursor)
def get_all_cards_for_user(userId):
    query = f"SELECT * FROM usercards WHERE userId={userId}"
    cursor.execute(query)
    alluserCards = map_usercards(cursor)
    allCards = []
    for userCard in alluserCards:
        card = get_card(userCard.cardId)
        allCards.append(card)
    return allCards
def get_all_cards():
    query = "SELECT * FROM card"
    cursor.execute(query)
    return map_cards(cursor)
def empty_cards_table():
    cursor.execute("DELETE FROM card")
def empty_usercards_table():
    cursor.execute("DELETE FROM usercards")
def empty_user_table():
    cursor.execute("DELETE FROM card")  
#mapping
def map_user(cursorUserResult):
    if cursorUserResult:
        users = [] 
        for x in cursorUserResult:
            users.append(User(x[0],x[1],bool(x[2])))
        return users
    else:
        print("Cursor returned no values")
        return None
def map_usercards(cursorUserCardsResult):
    if cursorUserCardsResult:
        userCards = [] 
        for x in cursorUserCardsResult:
            userCards.append(UserCards(x[0],x[1],x[2]))
        return userCards
    else:
        print("Cursor returned no values")
        return None
def map_cards(cursorCardResult):
    
    if cursorCardResult:
        cards = [] 
        for x in cursorCardResult:
            thisCard = Card(x[6],x[0],x[1],x[2],x[3],x[4],x[6])
            cards.append(thisCard)
        return cards
    else:
        print("Cursor returned no values")
        return None

#classes
class Card: 
    def __init__(self, cardId,veefriend,coreImageLink,score,aura,skill,stamina):
        self.cardId = cardId
        self.veefriend = veefriend
        self.coreImageLink = coreImageLink
        self.score = score
        self.aura = aura
        self.skill = skill
        self.stamina = stamina

class UserCards:      
    def __init__(self,cardId, userId, rarity):
        self.cardId = cardId
        self.userId = userId
        self.rarity = rarity
class User:
    def __init__(self,userId, username, isDiscordVerified):
        self.userId = userId
        self.username = username
        self.isDiscordVerified = isDiscordVerified
#enums
class CardRarity(Enum):
    CORE = 1
    RARE = 2
    VERYRARE = 3
    EPIC = 4
    SPEC = 5
    VF1EDITION = 6
    GIFTGOAT = 7
    AUTO = 8

# user = get_user_by_discord_id("209417071845441536")
# print("x")
