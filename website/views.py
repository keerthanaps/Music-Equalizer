from flask import Blueprint, render_template, request,redirect,send_file, flash, jsonify
from flask_login import login_required, current_user
from . import db
import os
from werkzeug.utils import secure_filename


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please select a file.',category='error')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        
        if file.filename == '':
            flash('Please select a file.',category='error')
            return redirect(request.url)
        else:
            file = request.files["file"]
            file.save(os.path.join("/home/keerthana/Flask-Web-App-Tutorial/uploads",file.filename))
            print("saved")
            flash('Your file is being processed and downloaded. Please Wait!', category='success')

            return redirect(request.url)

    return render_template("home.html", user=current_user)




