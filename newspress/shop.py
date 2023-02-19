from flask import (
    flash, Blueprint, request, redirect, render_template, g, url_for
)
from werkzeug.utils import secure_filename

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
    return render_template('shop.html', products=products)

@blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_new_product():
    ''' Create a new product and save it to the database '''
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        category = request.form['category']
        description = request.form['description']
        additional_info = request.form['additional_info']
        review = request.form['review']
        photo = secure_filename(request.files['photo'].filename)

        error = None
        db = get_database()

        if not title:
            error = 'Title is required'
        elif not price or int(price) < 0:
            error = 'Invalid price'
        elif not category:
            error = 'Category is required'
        elif not description:
            error = 'Product description is required'
        elif not additional_info:
            error = 'Product additional information is required'
        elif not review:
            error = 'Product review is required'
        elif not photo:
            error = 'Please include the product photo'
        if error is not None:
            flash(error)
        else:
            db.execute(
                ''' INSERT INTO products (title, price, description, category, additional_info,
                                        review, photo, seller_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (title, price, description, category,additional_info,review, photo, g.user.id)
            )
            db.commit()
            return redirect(url_for('shop.get_all_products'))

    return render_template('new-product.html')
