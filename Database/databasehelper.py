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
cursor = db.cursor()

def create_user(username, discordId):
    cursor.execute("INSERT INTO user (username, discordid) VALUES (%s,%s)", (username,discordId))
    db.commit()
    createdUserId = cursor.lastrowid
    cursor.execute(f"SELECT * FROM user WHERE userId = {createdUserId}")
    return map_user(cursor)[0]
def create_card(veefriend, score, aura, skill,stamina,rarity, coreImageLink):
    cursor.execute("INSERT INTO card (veefriend, score, aura, skill, stamina, rarity, coreImageLink) VALUES (%s,%s,%s,%s,%s,%s,%s)", (veefriend,score,aura,skill,stamina,rarity,coreImageLink))
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
    return map_user(cursor.execute(f"SELECT * FROM user WHERE userId={userId}"))
def get_card(cardId):
    return map_cards(cursor.execute(f"SELECT * FROM card WHERE cardId={cardId}"))
def get_all_cards_for_user(userId):
    return map_cards(cursor.execute(f"SELECT * FROM usercards WHERE userId={userId}"))
def get_all_cards():
    return map_cards(cursor.execute(f"SELECT * FROM card"))
def empty_cards_table():
    cursor.execute("DELETE FROM card")

#mapping
def map_user(cursorUserResult):
    users = [] 
    for x in cursorUserResult:
        users.append(User(x[0],x[1],bool(x[2])))
    return users
def map_cards(cursorCardResult):
    cards = [] 
    for x in cursorCardResult:
        cards.append(Card(x[5],x[0],x[1],x[2],x[3],x[4],x[6]))
    return cards

#classes
class Card: 
    def __init__(self, cardId,veefriend,score,aura,skill,stamina,rarity):
        self.cardId = cardId
        self.veefriend = veefriend
        self.score = score
        self.aura = aura
        self.skill = skill
        self.stamina = stamina
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
