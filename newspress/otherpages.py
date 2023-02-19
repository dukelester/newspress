from flask import (
    request, render_template, g, current_app, Blueprint, redirect, url_for, flash
)

from newspress.database import get_database

blueprint = Blueprint('contact_us', __name__)

@blueprint.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    ''' Contact us'''
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        comment = request.form['comment']

        db = get_database()
        error = None

        if not first_name:
            error = 'First name is required'
        elif not last_name:
            error = 'Last name is required'
        elif not email:
            error = 'Email is required'
        elif not phone:
            error = 'Phone number is required'
        elif not subject:
            error = 'Subject is required'
        elif not comment:
            error = 'The comment is required'
        if error is not None:
            flash(error)
        else:
            db.execute(
                ''' INSERT INTO contact (first_name, last_name, email, phone, subject, comment)
                VALUES (?, ?, ?, ?, ?, ?)
                ''',
                (first_name, last_name, email, phone, subject, comment)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('contact.html')
