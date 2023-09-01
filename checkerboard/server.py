from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkers(x, y, color1, color2):
    # row= int(x)
    # column = int(y)
    return render_template('index.html', row=x, column=y, color1=color1, color2=color2)


if __name__=="__main__": 
    app.run(debug=True)