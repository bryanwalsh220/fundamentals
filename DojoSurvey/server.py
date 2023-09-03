from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "keep it a secret"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def processSurvey():
    print("got the info")
    print(request.form)
    session['name']=request.form['name']
    session['location'] = request.form['dojoLocation']
    session['languages'] = request.form['languages']
    # session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    print('Showing Results of Survery')
    print(request.form)
    return render_template('results.html', name_on_template=session['name'], location_on_template=session['location'], languages_on_template=session['languages'])

if __name__=="__main__":   
    app.run(debug=True)    