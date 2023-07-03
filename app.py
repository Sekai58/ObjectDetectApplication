from flask import Flask,request, render_template,redirect,url_for;
from werkzeug.utils import secure_filename
import os


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
    sentence = request.form['disc']
    file = request.files.getlist('myFile')
    print(file,sentence)
    path = []
    files = []
    for f in file:
        filename = secure_filename(f.filename)
        #path.append("images/" + f.filename)
        files.append(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return redirect(url_for('upload'))

if __name__ == '__main__':
    app.run(debug=True)