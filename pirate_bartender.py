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

drink_preferences = {}
special_drink = []
customers = {}

def drink_questions():
    """this function asks questions to figure out your drink"""
    for key, value in questions.items():
        x =raw_input("{}  ".format(value))
        if x=="y" or x=="yes":
            drink_preferences[key] = True
        else:
            drink_preferences[key] = False
    return drink_preferences

def drink_maker():
    """this question makes your drink"""
    for x, y in drink_preferences.items():
        if y==True:
            special_drink.append(random.choice(ingredients[x]))
    return special_drink

def drink_checker():
    """
    This checker asks your name to see if you have ordered a drink before.
    If you have ordered a drink before, it gives you the same drink.
    Else it creates a new drink for you.
    If you want another drink it will give you another drink, either the same or random???
    This will also check whether you created a "non-drink" with all false preferences.
    It will also give the drink a name if appropriate.
    And reduce the supplies if appropriate.
    """
    matey = raw_input("Hi there matey, what is your name?  ")
    if matey in customers:
        print("Welcome back {}! Here is a drink, the way you like it:".format(matey))
        for x in customers[matey]:
            print(', '.join(customers[matey]))    
    else:
        drink_questions()
        new_drink = drink_maker()
        customers[matey] = new_drink

if __name__ == '__main__':
    print("Drink Preferences Before:  " + str(drink_preferences))
    print("Special Drink Before:  " + str(special_drink))
    print("Customers Before:  " + str(customers))
    drink_checker()
    print("Drink Preferences After:  " + str(drink_preferences))
    print("Special Drink After:  " + str(special_drink))
    print("Customers After:  " + str(customers))
    