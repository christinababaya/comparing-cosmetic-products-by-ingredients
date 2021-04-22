"""Models for cosmetics comparism."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()



class Product(db.Model):
    """Products."""

    __tablename__ = 'products'

    product_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        nullable=False)
    name = db.Column(db.String)
    brand = db.Column(db.String)
    product_categorization = db.Column(db.String)
    image = db.Column(db.String)

    def __repr__(self):
        return f'<Product product_id={self.product_id} name={self.name} brand={self.brand} product_categorization={self.product_categorization} image={self.image}>'


class Ingredient(db.Model):
    """Chemicals.. What the ingredients do."""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        nullable=False)
    ingredient_name = db.Column(db.String)

    def __repr__(self):
        return f'<Ingredient ingredient_id={self.ingredient_id} name={self.ingredient_name}>'


class Product_Ingredient(db.Model):
    """Product ingredients"""

    __tablename__ = 'product_ingredients'
    
    product_ingredient_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True,
                            nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))

    product = db.relationship('Product', backref='product_ingredients')
    ingredient = db.relationship('Ingredient', backref='product_ingredients')

    def __repr__(self):
        return f'<Product_Ingredient product_ingredient_id={self.product_ingredient_id} product_id={self.product_id} ingredient_id={self.ingredient_id}>'


class Review(db.Model):
    """Customer Reviews"""

    ___tablename___ = 'reviews'

    review_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True,
                            nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))

    product = db.relationship('Product', backref='reviews')

    def __repr__(self):
        return f'<Review review_id={self.review_id} product_id={self.product_id}>'


def connect_to_db(flask_app, db_uri='postgresql:///cosmetics', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False)