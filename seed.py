"""Script to seed database."""

import os
from datetime import datetime

import crud
import model
import server

os.system('dropdb comparing-cosmetic-products-by-ingredients')
os.system('createdb comparing-cosmetic-products-by-ingredients')

model.connect_to_db(server.app)
model.db.create_all()


SEED =
 #GET/ products
    #returns list of all porducts
    {
        'product': {
            "id": 1,
            "brand": "amorepacific",
            "name": "age spot brightening pen",
            "ingredients": [
                "water",
                "butylene glycol",
                "alcohol",
                ]
    },
    {
        "id": 2,
        "brand": "amorepacific",
        "name": "all day balancing care serum",
        "ingredients": [
            "camellia sinensis leaf water",
            "phyllostachis bambusoides juice",
            "panax ginseng root extract",
        ]
    },
    {
        "id": 3,
        "brand": "amorepacific",
        "name": "bio-enzyme refining complex",
        "ingredients": [
            "panax ginseng root extract",
            "cyclopentasiloxane",
            "dimethicone",
        ]
    },
]

    {
        #GET /products/1
        #returns a single product by id number
    "id": 1,
    "brand": "amorepacific",
    "name": "age spot brightening pen",
    "ingredient_list": [
        "water",
        "butylene glycol",
        "alcohol",
        "dipropylene glycol",
        "peg-75",
        "glycereth-26",
        "ascorbyl glucoside",
    ]
    },

    #POST /products
#Adds a product, new ingredients are added to the ingredient database
#Accepted params (all fields must be present):
#brand (string)
#name (string)
#ingredients (string, separated by commas) ex. "water,alcohol,citric acid,..."
[ 
     {
         #GET /ingredients
         #returns a list of all unique ingredients
        "id": 1,
        "ingredient": "water"
    },
    {
        "id": 2,
        "ingredient": "butylene glycol"
    },
    {
        "id": 3,
        "ingredient": "alcohol"
    },
]
[
    {
        #GET /ingredient?q=rose+water
        #Searches ingredient for LIKE values
        "id": 2493,
        "ingredient": "rose water"
    },
    {
        "id": 3103,
        "ingredient": "damask rose water"
    }
]

for i in SEED:    

    username = SEED[i]['info']['username']
    email = SEED[i]['info']['email']
    password = SEED[i]['info']['password']
    name = SEED[i]['info']['name']
    location = SEED[i]['info']['location']
    about = SEED[i]['info']['about']
    member_since = SEED[i]['info']['member_since']

    description = SEED[i]['cleanse']['description']
    start_date = SEED[i]['cleanse']['start_date']
    end_date = SEED[i]['cleanse']['end_date']
    public = SEED[i]['cleanse']['public']
    active = SEED[i]['cleanse']['active']
    completed = SEED[i]['cleanse']['completed']

    clog_timestamp = SEED[i]['cleanse_log']['timestamp']
    comment = SEED[i]['cleanse_log']['comment']
    private = SEED[i]['cleanse_log']['private']

    r_name = SEED[i]['recipe']['name']
    timestamp = SEED[i]['recipe']['timestamp']
    

    i_name = SEED[i]['ingredients'][1]['name']
    calories = SEED[i]['ingredients'][1]['calories']
    i_name_2 = SEED[i]['ingredients'][2]['name']
    calories_2 = SEED[i]['ingredients'][2]['calories']
    i_name_3 = SEED[i]['ingredients'][3]['name']
    calories_3 = SEED[i]['ingredients'][3]['calories']




    db_user = crud.create_user(username, email, password, name, location, about, member_since)
    db_ingredient = crud.create_ingredient(i_name, calories)
    db_ingredient_2 = crud.create_ingredient(i_name_2, calories_2)
    db_ingredient_3 = crud.create_ingredient(i_name_3, calories_3)
    db_recipe = crud.create_recipe(r_name, db_user)
    db_cleanse = crud.create_cleanse(start_date, end_date, public, description, db_user)

    crud.create_recipe_ingredient(db_recipe, db_ingredient)
    crud.create_recipe_ingredient(db_recipe, db_ingredient_2)
    crud.create_recipe_ingredient(db_recipe, db_ingredient_3)

    db_user_cleanse = crud.create_user_cleanse(active, completed, db_cleanse, db_user)
    crud.create_user_cleanse_recipe(timestamp, start_date, db_user_cleanse, db_recipe)
    crud.create_cleanse_log(clog_timestamp, comment, private, db_user_cleanse)


