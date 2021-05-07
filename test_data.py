"""test data for database"""
from unittest import TestCase
from server import app
from model import connect_to_db, db
from flask import session



from model import db, Product, Ingredients, Product_ingredients, Suggestions, connect_to_db

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy



class FlaskTests(TestCase):
    """Tests for the Flask server"""

    def setUp(self):
        """Setup code to run before every test."""

        
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
        
        connect_to_db(server.app)
        db.create_all()
        test_seed.create_test_data()


    def test_homepage(self):
        """Test homepage to see if it can be reached"""

        result = self.client.get("/")
        self.assertIn(b"Welcome!", result.data)





if __name__ == "__main__":
    import unittest

    unittest.main()