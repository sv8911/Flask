from flask import Flask

##wsgi application
app=Flask(__name__)
@app.route('/') #decorator 
def welcome():
    return 'Welcome pretty people heleo'
@app.route('/memebers') #decorator 
def members():
    return 'Welcome pretty people cutus'

    
if __name__=='__main__':
    app.run(debug= True)   