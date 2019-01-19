# This session used for navigationbar
# also this session using for reading data from data.py and shows cardview, it is 2nd phase


# Below is Flask library importing statement
# render_template for rendering html page
# flask,data from their files name like data.py->data
from flask import Flask,render_template

# import Faculties() fn name from data.py
from data import Faculties


# __ double under score means it is special type of variables in python
# __name__ add to Flask
app = Flask(__name__)

# set Faculties() fn values from data.py to set to myFaculties list

myFaculties = Faculties()

# routing set
# what to do when / set
# we are set route with message hello
# so we need to create fn called index() it may be whatever name,
# then return hello
@app.route('/')
def index():
     return 'Hello'

# another routings
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    # return 'Register'
    # below is for seeing html content
    #  return "<h1>Register Page</h1>"

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # return render_template('index.html')
     return render_template('dashboard.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/io')
def main():
    return render_template('master.html')


@app.route('/faculty')
def faculty():
    # return render_template('faculty.html')

    # myFaculties value set to facultyList for looping data in html page
    return render_template('faculty.html',facultyList = myFaculties)


# running from main,tell to flask it is main file, app start from this file
# cross check __name__ values is equal to __main__, if it is equal app run.
# if it is preliminary this file run
if(__name__ == '__main__'):
    # app.run()
    # below debug for , we no need to stop every time,just enable debug true,then refresh page
     app.run(debug=True)

    # python app.py
    # then app run  on http://127.0.0.1:5000/
    # but in chrome copy paste show error Notfound error
    # error because, route not set(/ not set) //routing not set
    # preliminary is slash(/),but flask not identify
    # so we need to set routing
    # so we need to write code like above @app to return hello , for routing
    # for routing 17 to 19 step using


    

