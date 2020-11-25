from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

variables_list = ['tipoEgreso' , 'tipoElemento' , 'proveedor', 'formaPago', 'aprobacion', 'realizarPago']


@app.route('/compras', methods=['GET'])
def get_compras():
    all_compras = requests.get('http://localhost:5000/compras').json()
    return render_template('index.html', compras=all_compras)


@app.route('/compras', methods=['POST'])
def create_compra():
    compra = dict(request.values)
    compra['tipoEgreso'] = compra['tipoEgreso']
    compra['tipoElemento'] = compra['tipoElemento']
    compra['proveedor'] = compra['proveedor']
    compra['formaPago'] = compra['formaPago']
    compra['aprobacion'] = compra['aprobacion']
    compra['realizarPago'] = compra['realizarPago']
    requests.post('http://localhost:5000/compras', json=compra)
    return(get_compras())

#app.run(port=8000, debug=True)
