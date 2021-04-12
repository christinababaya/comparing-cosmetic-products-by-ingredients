"""CRUD opperations"""

from model import db, Product, Ingredients, Product_ingredients, Review, connect_to_db

def create_product(name, name_brand, product_categorization, image):
    """Create and return a new product."""

    product = Product(name=name, name_brand=name_brand, product_categorization=product_categorization, image=image)

    db.session.add(product)
    db.session.commit()

    return product

def create_ingredients(ingredients):
    """Create a return the ingredients."""

    ingredients = Ingredients(ingredients=ingredients)

    db.session.add(ingredients)
    db.session.commit()

    return ingredients

def create_review(product):
    """"Create and return reviews"""

    review = Review(uproduct=product)
    
    db.session.add(review)
    db.session.commit()

    return review

if __name__ == '__main__':
    from server import app
    connect_to_db(app)