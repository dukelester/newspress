from flask import (
    flash, Blueprint, request, redirect, render_template
)

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
    print(products, 'products')
    return render_template('shop.html', products=products)
