from flask import Flask,request, render_template,redirect,url_for;
from werkzeug.utils import secure_filename
import os

import objectdetection

app = Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\zeroa\\amrita\\test_prj\\objectDetect\\static\\images'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=['GET','POST'])
def upload():
    return render_template('upload.html')

@app.route("/uploaded",methods=['GET','POST'])
def uploaded():
    file = request.files['myFile']
    print(file,sentence)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
    label, cordinate = objectdetection.getCordinates( file.filename)
    print(label,cordinate)
    return redirect(url_for('upload'))

if __name__ == '__main__':
    app.run(debug=True)