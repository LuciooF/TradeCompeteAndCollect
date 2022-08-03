
# TradeCompeteAndCollect

This project is an OpenSource project with very basic (junior leve) code to create a 
simple website with the goal of easing the trade process of Compete And Collect cards (These are cards related to GaryVee and his Veefriends NFT project.)


The idea is to have a simple website where you can show what cards you have in your deck, and you can share this to anyone who wants to trade with you, they can create their deck and you can compare, and get to a deal.

There will be, also, filtering to ease the process. Like, you can compare between to decks, and filter what cards you have, that the other person doesnt, and viceversa.


## Features

- Create user and save your deck (connect via discord)
- Compare decks with another user
- Share link to show your deck


## Contributing

Contributions are always welcome!

If you'd like to help out, feel free to contact me on discord (LuciooF#8959).

Create a dev branch and have fun with it!


## Setup

To get this set up, download mySql, setup as default, take note of your host, password and database name

Create a .env file with the following
```env
DBUSER=(YourDBUser)
DBNAME=(YourDBName)
DBPASSWORD=(YourDBPassowrd)
```
In MySQL workbench, run the following queries (In this order)
```sql
CREATE TABLE card
  (
     veefriend     VARCHAR(100),
     coreimagelink VARCHAR(100),
     score         SMALLINT,
     aura          SMALLINT UNSIGNED,
     skill         SMALLINT UNSIGNED,
     stamina       SMALLINT UNSIGNED,
     rarity        ENUM ('core', 'rare', 'veryrare', 'epic', 'spec',
     'vf1edition',
     'giftgoat',
     'auto'),
     cardid        INT PRIMARY KEY auto_increment
  ); 
```
```sql
CREATE TABLE user
  (
     userid            INT PRIMARY KEY auto_increment,
     username          VARCHAR(50) NOT NULL UNIQUE,
     isdiscordverified BOOLEAN NOT NULL
  ); 
```
```sql
CREATE TABLE usercards
  (
     cardid INT,
     userid INT,
     FOREIGN KEY (cardid) REFERENCES card (cardid),
     FOREIGN KEY (userid) REFERENCES USER (userid) ON DELETE CASCADE
  ) 
```

