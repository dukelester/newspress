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
    db = get_database()
    blog_posts = db.execute(
        ''' SELECT p.id, title, body, category, created_at, photo, video_url, tags
            FROM blog p JOIN user u ON p.author_id = u.id
            ORDER BY created_at DESC
        '''
    ).fetchall()
    print(blog_posts)
    return render_template('index.html', blog_posts=blog_posts)
