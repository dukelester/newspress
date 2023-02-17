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

@blueprint.route('/create', methods=['POST', 'GET'])
@login_required
def create_new_blog():
    ''' Create a new blog '''
    if request.method == 'POST':
        title =  request.form['title']
        body = request.form['body']
        category = request.form['category']
        photo = request.files['photo']
        video_url = request.files['video_url']
        tags = request.files['tags']

        db = get_database()
        error = None
        if not title:
            error = 'Title is required'
        elif not body:
            error = 'The body is required'
        elif not category:
            error = 'Category is required'
        elif not photo:
            error = 'Photo is required'
        elif not video_url:
            error = 'Video url is needed'
        elif not tags:
            error = 'Tags are required'
        if error is not None:
            flash(error)
        else:
            db.execute(
                ''' INSERT INTO blog (title, body, category, photo, tags, video_url, author_id),
                VALUES (?, ?, ?, ?, ?, ?, g.user['id'])
                '''
            ).commit()
            return redirect(url_for('blog.index'))
    return render_template('create-blog.html')
