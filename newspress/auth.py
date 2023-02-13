''' The blueprint for authentication views '''
import functools
from flask import (
    redirect, render_template, g, flash, request, session, url_for, Blueprint,
)
from werkzeug.security import check_password_hash, generate_password_hash
from newspress.database import get_database

blueprint = Blueprint('auth', __name__, url_prefix='/auth')
