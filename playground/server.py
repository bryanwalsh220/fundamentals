from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:num>/<color>')
def play(num, color):
    num_boxes = int(num)
    return render_template('play.html', num_boxes=num_boxes, color=color)



if __name__=="__main__": 
    app.run(debug=True)