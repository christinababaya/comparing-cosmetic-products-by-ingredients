"""Server for Xtina Metics app."""

from flask import (Flask , render_template, request, flash, session, redirect)
from model import connect_to_dbe
import crud
from jinja2 import StrictUndefined



app = Flask(__name__)
app.secrete_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/products')
def all_products():
    """View all products."""

    products = crud.get_products()

    return render_template('all_products.html', products=products)


@app.route('/products/<product_id>')
def show_product(product_id):
    """Show details on a particular product."""

    product = crud.get_product_by_name(name)

    return render_template('product_details.html', product=product)


@app.route('/ingredients')
def all_products():
    """View all ingredients."""

    ingredients = crud.get_ingredients()

    return render_template('all_product_ingredients.html', ingredients=ingredients)


@app.route('/ingredients/<ingredient_id>')
def show_product(product_id):
    """Show details on a particular product ingredient."""

    ingredient = crud.get_ingredient_by_name(ingredient_name)

    return render_template('ingredient_details.html', ingredient=ingredient)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
