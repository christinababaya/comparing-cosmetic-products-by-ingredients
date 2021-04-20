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

