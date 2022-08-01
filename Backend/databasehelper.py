import mysql.connector

db = mysql.connector.connect(
    host="SOMEHOST",
    user="SOMEUSER",
    passwd = "SOMEPSWD",
    database="SOMEDB"
)
cursor = db.cursor()

#Enums for rarity (core, rare, veryrare, epic, spec, vf1edition, giftgoat, auto)
cursor.execute("CREATE TABLE Card (veefriend VARCHAR(50), score smallint, aura smallint UNSIGNED, skill smallint UNSIGNED, stamina smallint UNSIGNED, rarity ENUM ('core','rare','veryrare','epic','spec','vf1edition','giftgoat','auto'), cardID int PRIMARY KEY AUTO_INCREMENT)")
cursor.execute("CREATE TABLE User (userId INT unsigned NOT NULL AUTO_INCREMENT,username VARCHAR(50) NOT NULL,isDiscordVerified BOOLEAN NOT NULL,PRIMARY KEY (userId));")
cursor.execute("CREATE TABLE UserCards (cardId INT NOT NULL, userId INT NOT NULL, FOREIGN KEY (cardId) REFERENCES Card (cardId), FOREIGN KEY (userId) REFERENCES User (userId))")

print("\nUser Table")
cursor.execute("DESCRIBE User")
for x in cursor:
    print(x)
print("\nCard Table")
cursor.execute("DESCRIBE Card")
for x in cursor:
    print(x)
print("\nUserCards Table")
cursor.execute("DESCRIBE UserCards")
for x in cursor:
    print(x)