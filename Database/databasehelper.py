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
    database="CCTEST"
)
cursor = db.cursor()

# cursor.execute("CREATE TABLE Card (veefriend VARCHAR(50), score smallint, aura smallint UNSIGNED, skill smallint UNSIGNED, stamina smallint UNSIGNED, rarity ENUM ('core','rare','veryrare','epic','spec','vf1edition','giftgoat','auto'), cardID int PRIMARY KEY AUTO_INCREMENT)")
# cursor.execute("CREATE TABLE User (userId INT unsigned NOT NULL AUTO_INCREMENT,username VARCHAR(50) NOT NULL,isDiscordVerified BOOLEAN NOT NULL,PRIMARY KEY (userId));")
# cursor.execute("CREATE TABLE UserCards (cardId INT NOT NULL, userId INT NOT NULL, FOREIGN KEY (cardId) REFERENCES Card (cardId), FOREIGN KEY (userId) REFERENCES User (userId))")

#actual database queries
def create_user(username, isDiscordVerified):
    cursor.execute("INSERT INTO user (username, isDiscordVerified) VALUES (%s,%s)", (username,isDiscordVerified))
    db.commit()
def create_card(veefriend, score, aura, skill,stamina,rarity):
    cursor.execute("INSERT INTO card (veefriend, score, aura, skill, stamina, rarity) VALUES (%s,%s,%s,%s,%s,%s)", (veefriend,score,aura,skill,stamina,rarity))
    db.commit()
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


#user = create_user("LuciooF2", False)
#card = create_card("Lemur",50,20,10,5,CardRarity.RARE.value)
#add_card_to_user(3,7)
remove_card_from_user(3,7)
remove_user(3)
print("s")
#interpretator








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