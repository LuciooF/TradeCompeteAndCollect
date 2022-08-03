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
    user="root",
    passwd = os.getenv("DBPASSWORD"),
    database="test"
)
cursor = db.cursor()

#initial db setup
# cursor.execute("CREATE TABLE Card (veefriend VARCHAR(100), coreImageLink VARCHAR(100), score smallint, aura smallint UNSIGNED, skill smallint UNSIGNED, stamina smallint UNSIGNED, rarity ENUM ('core','rare','veryrare','epic','spec','vf1edition','giftgoat','auto'), cardId int PRIMARY KEY AUTO_INCREMENT)")
# cursor.execute("CREATE TABLE User (userId INT PRIMARY KEY AUTO_INCREMENT,username VARCHAR(50) NOT NULL UNIQUE,isDiscordVerified BOOLEAN NOT NULL);")
# cursor.execute("CREATE TABLE UserCards (cardId INT, userId INT, FOREIGN KEY (cardId) REFERENCES Card (cardId), FOREIGN KEY (userId) REFERENCES User (userId) ON DELETE CASCADE)")


#actual database queries
def create_user(username, isDiscordVerified):
    cursor.execute("INSERT INTO user (username, isDiscordVerified) VALUES (%s,%s)", (username,isDiscordVerified))
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



#Testing normal functionality
# user = create_user(str(datetime.now()), False)
# card = create_card("Lemur",50,20,10,5,CardRarity.RARE.value)
# print(f"Adding card id {card.cardId} to user {user.userId}")
# add_card_to_user(user.userId,card.cardId)
# remove_card_from_user(user.userId,card.cardId)
# remove_user(user.userId)








# print("\nUser Table")
# cursor.execute("DESCRIBE User")
# for x in cursor:
#     print(x)
# print("\nCard Table")
# cursor.execute("DESCRIBE Card")
# for x in cursor:
#     print(x)
# print("\nUserCards Table")
# cursor.execute("DESCRIBE UserCards")
# for x in cursor:
#     print(x)