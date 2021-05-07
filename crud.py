"""CRUD opperations"""

from model import db, Product, Ingredient, Product_Ingredient, connect_to_db
from sqlalchemy import or_

def create_product(name, brand, product_categorization, image=''):
    """Create, add to db, and return a new product."""

    product = Product(name=name, brand=brand, product_categorization=product_categorization, image=image)

    db.session.add(product)
    db.session.commit()

    return product


def get_all_products():
    """Returns all products in database in a list"""

    return Product.query.all()

def get_product_by_ingredient(ingredient):
    """gets the ingrgedients"""

    # ingredient_input = Ingredient.query.filter_by(ingredient_name=ingredient)
    return Product_Ingredient.query.filter_by(ingredient_id=ingredient.ingredient_id)
    # ingredientId = Ingredient.query.filter_by(ingredient=ingredient).get(ingredient_name)
    # productId = Product_Ingredient.query.filter_by(ingredientId=ingredient_id)
    # return Product.query.get(productId)
    #return Product_Ingredient.query.filter_by(ingredient=ingredient.ingredient_name).get()

def search_products_by_substring(substring):
    """ Find products containing user submitted text. """
    
    return Product.query.filter(or_(Product.name.contains(substring),
                                    Product.brand.contains(substring),
                                    Product.product_categorization.contains(substring))
                                ).all()

def search_ingredients_by_substring(substring):
    """ Find ingredients containing user submitted text. """
    
    return Ingredient.query.filter(Ingredient.ingredient_name.contains(substring)).all()

def get_product_by_name(name):
    """Queries db for product by name and retrieves the first entry
    If no product exists, returns None."""
    
    return Product.query.filter_by(name=name).first()

def get_product_id(product_id):
    """Queries db for product by id."""

    return Product.query.get(product_id)


def create_ingredient(ingredient_name):
    """Create, add to db, and return an ingredient."""

    ingredient = Ingredient(ingredient_name=ingredient_name)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient


def get_all_ingredients():
    """Returns all ingredients in database in a list."""

    return Ingredient.query.all()


def get_ingredient_by_name(ingredient_name):
    """Queries db for ingredient by name and retrieves the first entry.
    If no ingredient exists, returns None."""
    
    return Ingredient.query.filter_by(ingredient_name=ingredient_name).first()

def get_ingredient_by_id(ingredient_id):
    """Queries db for ingrediente by id."""
    return Ingredient.query.get(ingredient_id)


def create_product_ingredient(product, ingredient):
    """
    Creates relationship between a product and one of its ingredients.
    Create, add to db, and return one product_ingredient.
    Each ingredient needs to be added separately for each product.
    """

    product_ingredient = Product_Ingredient(product_id=product.product_id, ingredient_id=ingredient.ingredient_id)

    db.session.add(product_ingredient)
    db.session.commit()

    return product_ingredient


def get_all_product_ingredients():
    """Returns all product ingredient relationships in a list."""

    return Product_Ingredient.query.all()


def get_prod_ing_by_prod_and_ing(product, ingredient):
    """Queries db for prod_ing by prod and ing and retrieves the first entry.
    If no prod_ing exists, returns None."""
    
    # return Product_Ingredient.query.filter_by(product=product, ingredient=ingredient).first()
    return db.session.query(Product_Ingredient).filter(Product_Ingredient.product_id==product.product_id, Product_Ingredient.ingredient_id==ingredient.ingredient_id).first()


def get_ingredients_for_product(product):
    """ Queries db for all prod_ing rows matching the product. """
    
    return Product_Ingredient.query.filter_by(product_id=product.product_id).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app, echo=False)