from flask import (
    request, render_template, g, current_app, Blueprint, redirect, url_for
)

blueprint = Blueprint('contact_us', __name__)

@blueprint.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    ''' Contact us'''
    if request.method == 'POST':
        pass
    return render_template('contact.html')
