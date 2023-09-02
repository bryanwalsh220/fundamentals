from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "key_secret"

@app.route('/count')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    
    session['visits'] += 1
    return render_template('index.html', visits=session['visits'])

@app.route('/destroy')
def reset_session():
    session.clear()
    return redirect('/count')

if __name__ == "__main__":
    app.run(debug=True)
