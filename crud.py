"""CRUD opperations"""

from model import db, Product, Ingredients, Product_ingredients, Review, connect_to_db

def create_product(name, name_brand, product_categorization, image):
    """Create and return a new product."""

    product = Product(name=name, name_brand=name_brand, product_categorization=product_categorization, image=image)

    db.session.add(product)
    db.session.commit()

    return product

def get_products():
    """Returns all products in database"""

    return Product.query.all()

def create_ingredients(ingredients):
    """Create a return the ingredients."""

    ingredients = Ingredients(ingredients=ingredients)

    db.session.add(ingredients)
    db.session.commit()

    return ingredients

def get_ingredients():
    """Returns all ingredients in database"""

    return Ingredients.query.all()

def create_product_ingredients(product, ingredients):
    """Creates relationship between a product and its ingredients"""

    product_ingredients = Product_ingredients(product=product, ingredients=ingredients)

    db.session.add(product_ingredients)
    db.session.commit()

    return product_ingredients

def get_product_ingredients():
    """Returns all product ingredient relationships"""

    return Product_ingredients.query.all()


def create_review(product):
    """"Create and return reviews"""

    review = Review(uproduct=product)
    
    db.session.add(review)
    db.session.commit()

    return review

def get_review():
    """Returns all reviews in database"""

    return Review.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)