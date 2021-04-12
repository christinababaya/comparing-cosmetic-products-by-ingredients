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

def create_review(user, movie, score):
    """"Create and return reviews"""

    review = Review(user= user, movie=movie, score=score)
    db.session.add(rating)
    db.session.commit()

    return review

if __name__ == '__main__':
    from server import app
    connect_to_db(app)