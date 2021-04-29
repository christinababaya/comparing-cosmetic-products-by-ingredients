"""Script to seed database."""

import os
# from datetime import datetime
import csv

import crud
import model
import server

os.system('dropdb cosmetics')
os.system('createdb cosmetics')

model.connect_to_db(server.app)
model.db.create_all()

#Load cosmetic data from CSV file
with open('data/chemicals-in-cosmetics-data.tsv') as tsv_f:
    f = csv.reader(tsv_f, delimiter="\t")
    count = 1

    for line in f:
        print('*******************************')
        print(count)
        print(line)
        print('*******************************')
        # line = line.rstrip()
        name, brand, product_categorization, ingredient_name = line
    
        product = crud.get_product_by_name(name)
        if product == None:
            product = crud.create_product(name=name, brand=brand, product_categorization=product_categorization)
        print('*******************************')
        print(product)
        print('*******************************')

        # product = crud.get_product_id(product_id)
        # if product == None:
        #     product = crud.create_product(product_id)
        # print('*******************************')
        # print(product)
        # print('*******************************')
        
        ingredient = crud.get_ingredient_by_name(ingredient_name)
        if ingredient == None:
            ingredient = crud.create_ingredient(ingredient_name)
        print('*******************************')
        print(ingredient)
        print('*******************************')
        
        product_ingredient = crud.get_prod_ing_by_prod_and_ing(product, ingredient)
        if product_ingredient == None:
            product_ingredient = crud.create_product_ingredient(product, ingredient)
        print('*******************************')
        print(product_ingredient)
        print('*******************************')
        
        count += 1







# SEED =
#  #GET/ products
#     #returns list of all porducts
#     {
#         'product': {
#             "id": 1,
#             "brand": "amorepacific",
#             "name": "age spot brightening pen",
#             "ingredients": [
#                 "water",
#                 "butylene glycol",
#                 "alcohol",
#                 ]
#     },
#     {
#         "id": 2,
#         "brand": "amorepacific",
#         "name": "all day balancing care serum",
#         "ingredients": [
#             "camellia sinensis leaf water",
#             "phyllostachis bambusoides juice",
#             "panax ginseng root extract",
#         ]
#     },
#     {
#         "id": 3,
#         "brand": "amorepacific",
#         "name": "bio-enzyme refining complex",
#         "ingredients": [
#             "panax ginseng root extract",
#             "cyclopentasiloxane",
#             "dimethicone",
#         ]
#     },
# ]

#     {
#         #GET /products/1
#         #returns a single product by id number
#     "id": 1,
#     "brand": "amorepacific",
#     "name": "age spot brightening pen",
#     "ingredient_list": [
#         "water",
#         "butylene glycol",
#         "alcohol",
#         "dipropylene glycol",
#         "peg-75",
#         "glycereth-26",
#         "ascorbyl glucoside",
#     ]
#     },

#     #POST /products
# #Adds a product, new ingredients are added to the ingredient database
# #Accepted params (all fields must be present):
# #brand (string)
# #name (string)
# #ingredients (string, separated by commas) ex. "water,alcohol,citric acid,..."
# [ 
#      {
#          #GET /ingredients
#          #returns a list of all unique ingredients
#         "id": 1,
#         "ingredient": "water"
#     },
#     {
#         "id": 2,
#         "ingredient": "butylene glycol"
#     },
#     {
#         "id": 3,
#         "ingredient": "alcohol"
#     },
# ]
# [
#     {
#         #GET /ingredient?q=rose+water
#         #Searches ingredient for LIKE values
#         "id": 2493,
#         "ingredient": "rose water"
#     },
#     {
#         "id": 3103,
#         "ingredient": "damask rose water"
#     }
# ]

