
# TradeCompeteAndCollect

This project is an OpenSource project with very basic (junior level) code to create a 
simple website with the goal of easing the trade process of Compete And Collect cards (These are cards related to GaryVee and his Veefriends NFT project.)


The idea is to have a simple website where you can show what cards you have in your deck, and you can share this to anyone who wants to trade with you, they can create their deck and you can compare, and get to a deal.

There will be, also, filtering to ease the process. Like, you can compare between two decks, and filter what cards you have, that the other person doesnt, and viceversa.


## Features

- Create user and save your deck (connect via discord)
- Compare decks with another user
- Share link to show your deck


## Contributing

Contributions are always welcome!

If you'd like to help out, feel free to contact me on discord (LuciooF#8959).

Create a dev branch and have fun with it!


## Setup

To get this set up, download MySQL, setup as default, take note of your host, password and database name

Change remove the .example from .env.example file and fill out those variables with your personal keys.

In MySQL workbench, run the following queries (In this order)
```sql
CREATE TABLE card
  (
     veefriend     VARCHAR(100),
     coreimagelink VARCHAR(100),
     score         SMALLINT UNSIGNED,
     aura          SMALLINT UNSIGNED,
     skill         SMALLINT UNSIGNED,
     stamina       SMALLINT UNSIGNED,
     cardid        INT PRIMARY KEY auto_increment
  ); 
```
```sql
CREATE TABLE user
  (
     userid            INT PRIMARY KEY auto_increment,
     username          VARCHAR(100) NOT NULL UNIQUE,
     discordid         VARCHAR(100) UNIQUE
  ); 
```
```sql
CREATE TABLE usercards
  (
     cardid INT,
     userid INT,
     rarity        ENUM ('core', 'rare', 'veryrare', 'epic', 'spec',
     'vf1edition',
     'giftgoat',
     'auto'),
     FOREIGN KEY (cardid) REFERENCES card (cardid),
     FOREIGN KEY (userid) REFERENCES USER (userid) ON DELETE CASCADE
  );
```
In MySQL go to Edit>Preferences... Untick "Safe updates(Rejects updates and Deletes with no restrictions) 

This is to allow
```python
empty_cards_table()
```
to clear the cards table each time this is ran.

Now execute populateCardsScript.py to populate the cards table with some data (This data is currently not full, but it is good enough for testing)

pip install all required packages

## Backend
### Set Up A Virtual Environment:

First thing need to do, is set up our virtual environment, a virtual environment helps us run several versions of python/django right on the same machine (e.g we could have two different python/django projects running on different versions, to avoid them clashing and to give us room to run them both without errors, the virtual environment comes to our rescue. One virtual environment = one python/django version).

### To set up our virtual environment:

- pip/pip3 install virtualenv

After installation, we should create a virtual environment that would enable us use a preferred django version of our choice:
- virtualenv env_name (env_name should be replaced with the preferred name of the environment)

### Activating Virtual Environment:
Now as we have setup our virtual env, we need to enable it, to enable the virtual env that we've just created (`env_name`):

To activate the virtual environment for linux/Mac OS:

- source env_name/bin/activate

For windows:

- env_name/scripts
- activate


### Install the required packages using:
Now it's time to create the required packages (including django):

- pip install -r requirements.txt

### Making Migrations:

Migrations helps us make changes to our database schema without losing any data, each time we create a new model or make changes to a current one and run migrations, it helps update our database tables with the schemas without having to go through all the stress of dragging and recreating the database ourselves.

To run our migrations:

- python manage.py migrate


### Run the project

- python manage.py runserver


## Frontend
First, you should have vue installed locally, if not run, npm install -g @vue/cli

To run the frontend: (default port 8080)

- cd frontend && yarn install
- yarn run serve
