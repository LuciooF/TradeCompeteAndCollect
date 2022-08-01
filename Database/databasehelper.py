import mysql.connector
import os
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
    cursor.execute(f"SELECT * FROM user WHERE userId={userId}")
    db.commit()
def get_card(cardId):
    cursor.execute(f"SELECT * FROM card WHERE cardId={cardId}")
    db.commit()
def get_all_cards_for_user(userId):
    cursor.execute(f"SELECT * FROM usercards WHERE userId={userId}")
    db.commit()
def get_all_cards():
    cursor.execute(f"SELECT * FROM card")
    db.commit()

#mapping
def map_user(cursorUserResult):
    users = [] 
    for x in cursorUserResult:
        users.append(
            {
                "userId": x[0],
                "username": x[1],
                "isDiscordVerified" : bool(x[2])
            }
        )
    return users
def map_card(cursorCardResult):
    cards = [] 
    for x in cursorCardResult:
        cards.append(
            {
                "cardId": x[5],
                "veefriend": x[0],
                "score" : x[1],
                "aura" : x[2],
                "skill" : x[3],
                "stamina" : x[4],
                "rarity" : x[6]
            }
        )
    return cards
cursor.execute("SELECT * FROM card")
allcards = map_card(cursor)
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