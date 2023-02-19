from flask import (
    flash, Blueprint, request, redirect, render_template, g, url_for
)
from werkzeug.utils import secure_filename
from werkzeug.exceptions import abort

from newspress.database import get_database
from newspress.auth import login_required


blueprint = Blueprint('shop', __name__, url_prefix='/shop')

@blueprint.route('/')
def get_all_products():
    ''' Display all the products in the shop '''
    db = get_database()
    products = db.execute(
        ''' SELECT * FROM products ORDER BY created_at '''
    ).fetchall()
    return render_template('shop.html', products=products, total=len(products))

@blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_new_product():
    ''' Create a new product and save it to the database '''
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        category = request.form['category']
        detailed_description = request.form['description']
        additional_info = request.form['additional_info']
        photo = secure_filename(request.files['photo'].filename)

        error = None
        db = get_database()

        if not title:
            error = 'Title is required'
        elif not price or int(price) < 0:
            error = 'Invalid price'
        elif not category:
            error = 'Category is required'
        elif not detailed_description:
            error = 'Product description is required'
        elif not additional_info:
            error = 'Product additional information is required'
        elif not photo:
            error = 'Please include the product photo'
        if error is not None:
            flash(error)
        else:
            db.execute(
                ''' INSERT INTO products (title, price, detailed_description,
                category, additional_info, photo, seller_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (title, price, detailed_description, category,additional_info, photo, g.user['id'])
            )
            db.commit()
            return redirect(url_for('shop.get_all_products'))

    return render_template('new-product.html')

def get_product_by_id(id, check_seller=True):
    ''' Get the product and return it based on its Id and return an error if not found '''
    db = get_database()
    product = db.execute(
        ''' SELECT * FROM products p JOIN user u ON p.seller_id = u.id
        WHERE p.id = ?
        ''',
        (id, )
    ).fetchone()
    if product is None:
        abort(404, f'Sorry the product with the id {id} can not be found...!')
    if check_seller and g.user is not None and product['seller_id'] != g.user['id']:
        abort(403)
    return product

@blueprint.route('/<int:id>')
def get_product_details_by_id(id):
    ''' Get a product details based on the product Id'''
    product = get_product_by_id(id)
    return render_template('shop-details.html', product=product)

@blueprint.route('<int:id>/update', methods=['POST', 'GET'])
def update_product_details_by_id(id):
    pass

@blueprint.route('/<int:id>/delete', methods=['POST', 'GET'])
def delete_product(id):
    pass