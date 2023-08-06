#Build url dynamically using Variable Rules
from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome"

@app.route('/success/<int:score>')
def success(score):
    return "marks is   "+ str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "marks is failed is "+ str(score)

##Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

#integrating html in flask
@app.route('/grades/<int:score>')
def grades(score):
    return "<html><body> <h1>The result is passsed </h1></body></html>" +str(score)


if __name__ =='__main__':
    app.run(debug=True)


