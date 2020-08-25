from flask import Flask
#create a new Flask app instance. 
# "Instance" is a general term in programming to refer to a singular version of something.
app = Flask(__name__) #magic method
#define starting point
@app.route('/') #forward slash (/) is the root of all the routes in the app
def hello_world():
    return 'Hello world'
