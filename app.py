from flask import *

from urllib.request import urlopen
from urllib.parse import quote
from pysmiles import read_smiles

import numpy as np
import networkx as nx
from networkx.algorithms import isomorphism


app = Flask(__name__)

def CIR_convert(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        return 'Did not work'


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
        
        s_formula1 = CIR_convert(c_name1)
        s_formula2 = CIR_convert(c_name2)
        
        adj_matrix_c1 = np.array([[0, 1, 0, 0, 0],
                          [1, 0, 1, 0, 1],
                          [0, 1, 0, 1, 1],
                          [0, 0, 1, 0, 1],
                          [0, 1, 1, 1, 0]])

        adj_matrix_c2 = np.array([[0, 1, 1, 1, 0],
                          [1, 0, 1, 0, 0],
                          [1, 1, 0, 1, 0],
                          [1, 0, 1, 0, 1],
                          [0, 0, 0, 1, 0]])
        G1 = nx.from_numpy_matrix(adj_matrix_c1)
        G2 = nx.from_numpy_matrix(adj_matrix_c2)
        GM = isomorphism.GraphMatcher(G1, G2)
        
        res = s_formula1
        return render_template("result.html", result=res)

if __name__ == '__main__':
    app.run(debug=True)
