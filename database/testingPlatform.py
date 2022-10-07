from databasehelper import * 
import random

#full test of user joining.

user = create_user(str(random.randint(0,1243255)),random.randint(1,1231))

firstCardId = random.randint(1,251) 

add_card_to_user(user.userId, firstCardId)
add_card_to_user(user.userId, random.randint(1,251))
add_card_to_user(user.userId, random.randint(1,251))
add_card_to_user(user.userId, random.randint(1,251))
add_card_to_user(user.userId, random.randint(1,251))

allcards = get_all_cards_for_user(user.userId)
print("This user has the following cards")
for dbObject in allcards:
    for card in dbObject:
        print(card.veefriend)

print(f"Removing card id {firstCardId}")
remove_card_from_user(user.userId, firstCardId)
allcards = get_all_cards_for_user(user.userId)
print("now, This user has the following cards")
for dbObject in allcards:
    for card in dbObject:
        print(card.veefriend)
print("Testing platform executed")

