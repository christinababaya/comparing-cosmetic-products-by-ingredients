"""test data for database"""
 


from model import db, Product, Ingredients, Product_ingredients, Review, connect_to_db

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy



def example_data():
    """Sample data to help with testing"""

    User.query.delete()
 
   

    db.session.add_all([ ])
    db.session.commit()





if __name__ == '__main__':
    from server import app

    connect_to_db(app)