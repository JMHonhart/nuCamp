'''
Flask Demo
By Jack Seymour
'''
import os
from werkzeug.utils import secure_filename
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

dn = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)


@app.route('/')
def index():
    '''
    Index
    '''
    resp = make_response(render_template('index_template.html'))
    if request.cookies.get('username') is None:
        resp.set_cookie('username', 'Captain Jack')
    return resp


@app.route('/home')
def home():
    '''
    Home Page
    '''
    return "Ye Cabin"


@app.route('/admin')
def admin():
    '''
    Admin Page
    '''
    return "Ye Bunker"


def do_login_post():
    '''
    Process POST
    '''
    return "Do the login POST"


def show_login_get():
    '''
    Login Page
    '''
    return "GET login page"


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Login
    '''
    if request.method == 'PSOT':
        return do_login_post()
    elif request.method == 'GET':
        return show_login_get()
    else:
        return "ERROR"


@app.route('/cookie')
def hello(_username=None):
    '''Render HTML Template Hello'''
    _username = request.cookies.get('username')
    return render_template('hello_template.html', name=_username)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    '''File Upload'''
    if request.method == 'POST':
        _file = request.files['the_file']
        # should do some type checking
        _path = os.path.join(os.path.join(dn, 'static/uploads'), secure_filename(_file.filename))
        print(f"Uploading {_file.filename} to {_path}")
        _image = '/static/uploads/' + secure_filename(_file.filename)
        _file.save(_path)
        # render our upload file
        return render_template('uploaded_template.html', file=_file.filename, image=_image)
    elif request.method == 'GET':
        return render_template('upload_template.html')
    else:
        return "ERROR"


# Allows to be run with python app.py
# alt use flask run -h localhost -p 8000
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=False)
