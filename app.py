from flask import *
from rdkit import Chem
from rdkit.Chem import Draw
from urllib.request import urlopen
from urllib.parse import quote
from pysmiles import read_smiles
import networkx as nx

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
        
        def CIR_convert(ids):
            try:
                url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
                ans = urlopen(url).read().decode('utf8')
                return ans
            except:
                return 'Did not work'
            
        s_formula1 = CIR_convert(mol1)
        
        res = s_formula1
        return render_template("result.html", result=res)

if __name__ == '__main__':
    app.run(debug=True)
