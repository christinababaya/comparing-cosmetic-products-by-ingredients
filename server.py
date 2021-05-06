"""Server for Xtina Metics app."""

from flask import (Flask , render_template, request, flash, session, redirect)
from model import connect_to_db
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
def allproducts():
    """View all products."""

    products = crud.get_all_products()

    return render_template('all_products.html', products=products)


@app.route('/products/<int:product_id>')
def show_product(product_id):
    """Show details on a particular product."""

    product = crud.get_product_id(product_id)
    product_ingredients = crud.get_ingredients_for_product(product)

    return render_template('product_details.html', product=product,
                           product_ingredients=product_ingredients)
    
@app.route('/products/search', methods=['GET'])
def search_products():
    """ Search product database for key term from user. """
    
    search_term = request.args.get('product_name')
    if not search_term:
        return redirect('/products')
    
    products = crud.search_products_by_substring(search_term)
    
    return render_template('product-results.html',
                           search_term=search_term, products=products)

# @app.route('/prodingredients')
# def all_product_ingredients():
#     """Show products with same ingredients."""

#     products = crud.get_product_by_ingredient("Estragole")

#     return render_template('results_page.html', ingredients=products)


@app.route('/ingredients')
def all_ingedients():
    """View all ingredients."""

    # ingredients = crud.get_product_by_ingredient("retinol")
    ingredients = crud.get_all_ingredients()

    return render_template('all_product_ingredients.html',
                           ingredients=ingredients)


@app.route('/ingredients/<int:ingredient_id>')
def show_ingredients(ingredient_id):
    """Show details on a particular ingredient."""

    ingredient = crud.get_ingredient_by_id(ingredient_id)
    ingredient_products = crud.get_product_by_ingredient(ingredient)

    return render_template('ingredient_details.html',
                           ingredient=ingredient,
                           ingredient_products=ingredient_products)


@app.route('/ingredients/search', methods=['GET'])
def search_ingredients():
    """ Search ingredients database for key term from user. """
    
    search_term = request.args.get('ingredient_name')
    if not search_term:
        return redirect('/ingredients')
    
    ingredients = crud.search_ingredients_by_substring(search_term)
    print('**************')
    print(ingredients)
    print('**************')
    
    return render_template('ingredient-results.html',
                           search_term=search_term, ingredients=ingredients)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
