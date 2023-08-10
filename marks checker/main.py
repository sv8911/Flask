#Integrate HTML with Flask
#HTTP verb GET and Post
##jinja template
from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"    
    exp={'score':score, 'res': res }
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', result=score)
#    return "marks is failed is "+ str(score)

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

#result checker html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        datascience=float(request.form['datascience'])
        C=float(request.form['C'])
        total_score=(science+maths+C+datascience)/4
    res=""
    if total_score>=50:
        res="success"
        return redirect(url_for(res,score=total_score))
    else:
        res="fail"    
        return redirect(url_for(res,score=total_score))




if __name__ =='__main__':
    app.run(debug=True)


