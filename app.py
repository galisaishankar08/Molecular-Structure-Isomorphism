from flask import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def output():
    return render_template('result.html')

@app.route('/', methods=['POST'])
def isomorphic():
    if request.method == "POST":
        mol1 = request.form["cname1"]
        mol2 = request.form["cname2"]
        
        res = mol1
        return render_template("result.html", result=res)

if __name__ == '__main__':
    app.run(debug=True)
