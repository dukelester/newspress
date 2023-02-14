from flask import (
    Blueprint, redirect, request, url_for, render_template, flash, g
)
from werkzeug.exceptions import abort

from newspress.auth import login_required
from newspress.database import get_database

blueprint = Blueprint('blog', __name__)

@blueprint.route('/')
def index():
    ''' The index route'''
    return render_template('index.html')
