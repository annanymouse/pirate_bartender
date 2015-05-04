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

def drink_questions():
    """this function asks questions to figure out your drink"""
    for key, value in questions.items():
        x =raw_input("{}  ".format(value))
        if x=="y" or x=="yes":
            drink_preferences[key] = True
        elif x=="n" or x=="no":
            drink_preferences[key] = False
        else:
            print("What is that there matey?  I will take that for a no.")
            drink_preferences[key] = False
    print(drink_preferences)
    return drink_preferences

def drink_maker():
    """this question makes your drink"""
    if True in drink_preferences.values():
        for key, value in drink_preferences.items():
            if value == True:
                for x, y in ingredients.items():
                    if key == x:
                        z = random.choice(ingredients[x])
                        print(z)
                        special_drink.append(z)
        #print("I'm gonna serve you a drink with {}, {}, {}, {}, {}...".format(*special_drink))
    else:
        print("Guessin' ye don't want a drink tonight, matey!!")

if __name__ == '__main__':
    #print(special_drink)
    drink_questions()
    #print(special_drink)
    drink_maker()
    #print("I'm gonna serve you a drink with {}, {}, {}, {}, {}...".format(*special_drink))