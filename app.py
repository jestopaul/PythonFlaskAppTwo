
# Below is Flask library importing statement
from flask import Flask


# __ double under score means it is special type of variables in python
# __name__ add to Flask
app = Flask(__name__)

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
    return 'Login'


@app.route('/register')
def register():
    # return 'Register'
    # below is for seeing html content
     return "<h1>Register Page</h1>"

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
    # for routing 15 to 17 step using


    

