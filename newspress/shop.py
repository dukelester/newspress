from flask import (
    flash, Blueprint, request, redirect, render_template
)

from newspress.database import get_database
from newspress.auth import login_required


blueprint = Blueprint('shop', __name__)

@blueprint.route('/')
def get_all_products():
    ''' Display all the products in the shop '''
    return render_template('shop.html')