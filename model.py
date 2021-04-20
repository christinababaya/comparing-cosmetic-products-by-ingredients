"""Models for cosmetics comparism."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()



# Replace this with your code!
class Product(dm.Model):
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


class Ingredients(db.Model):
    """Chemicals.. What the ingredients do."""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        nullable=True)
    ingredients = db.Column(db.String)

      def __repr__(self):
        return f'<Ingredients ingredient_id={self.ingredient_id} ingredients={self.ingredients}>'


class Product_ingredients(db.Model):
    """Product ingredients"""

    __tablename__ = 'product_ingredients'
    
    
    product_ingredients_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True,
                            nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey, ('products.product_id'))
    ingredients_id = db.Column(db.Integer, db.ForeignKey, ('products.ingredients_id'))

    product = db.relationship('Product', backref='product_ingredients')
    ingredients = db.relationship('Ingredients', backref='product_ingredients')

     def __repr__(self):
        return f'<Product_Ingredients product_ingredients_id={self.product_ingredients_id} product_id={self.product_id} ingredients_id={self.ingredients_id}>'

class Review(db.Model):
    """Customer Reviews"""

    ___tablename___ = 'review'


    review_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True,
                            nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey,('products.product_id'))

    product = db.relationship('Product', backref='review')

     def __repr__(self):
        return f'<Review review_id={self.review_id} product_id={self.product_id}>'

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
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

    connect_to_db(app)