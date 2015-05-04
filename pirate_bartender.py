"""
Pirate Bartender Project
"""
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = ['Salty', 'Fluffy', 'Sea Sick', 'Mad', 'Angry', 'Crazy', 'Electric']

nouns = ['Sea Dog', 'Chinchilla', 'Walrus', 'Shark', 'Eel', 'Whale', 'Jellyfish']

customers = {}

def drink_questions():
    """
    This function asks questions to figure out your drink.
    """
    drink_preferences = {}
    for key, value in questions.items():
        x = raw_input("{}  ".format(value))
        if x=="y" or x=="yes":
            drink_preferences[key] = True
        else:
            drink_preferences[key] = False
    return drink_preferences

def drink_mixer(my_dict):
    """
    This function mixes your drink.
    """
    special_drink = []
    for x, y in my_dict.items():
        if y==True:
            special_drink.append(random.choice(ingredients[x]))
    return special_drink

def drink_name():
    """
    This function names your drinks.
    """
    special_drink =  random.choice(adjectives) + " " + random.choice(nouns)
    print("I like to call it {}:".format(str(special_drink)))

def drink_creator():
    """
    This function call on two functions, drink_questions and drink_mixer, to create a drink.
    """
    a_dict = drink_questions()
    drink = drink_mixer(a_dict)
    return drink
    
def drink_checker():
    """
    This checker asks your name to see if you have ordered a drink before.
    If you have, it will ask if you want your usual or a new drink.
    If you are a new customer it creates a new drink for you.
    """
    matey = raw_input("What is your name?  ").lower()
    if matey in customers:
        drink = raw_input("Would you like your usual?  ").lower()
        if drink=="yes" or drink=='y':
            print("Welcome back {}! Here is your drink, the way you like it!".format(matey))
            drink_name()
            print("{}".format(str(customers[matey])))
        else:
            a_drink = drink_creator()
            print("Here's something new for you, {}".format(matey))
            drink_name()
            print(', '.join(a_drink))
    else:
        b_drink = drink_creator()
        customers[matey] = b_drink
        print("Welcome newbie, {}!  Here's yer drink!".format(matey))
        drink_name()
        print(', '.join(b_drink))

if __name__ == '__main__':
    while True:
        drinker = raw_input("Would you like a drink? ").lower()
        if drinker=='y' or drinker=='yes':
            drink_checker()
        else:
            print("Pleasure servin' ya, hope to see ya round these parts again soon!")
            break