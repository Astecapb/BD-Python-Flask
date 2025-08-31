from flask import Blueprint, request, jsonify # type: ignore
from sql_service2 import ClienteService

bp = Blueprint('clientes', __name__)


# ---- CRIAR CLIENTES ----
@bp.route('/clientes', methods=['POST'])
def criar_clientes():
    data = request.json
    cliente = ClienteService.criar(data['nome'], data['email'])
    return jsonify(cliente.to_dict()), 201

@bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = ClienteService.listar_clientes()
    return jsonify([c.to_dict() for c in clientes])

@bp.route('/clientes/<int:id>', methods=['GET'])
def buscar_clientes(id):
    cliente = ClienteService.buscar(id)
    return jsonify(cliente.to_dict()) if cliente else ('', 404)

@bp.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_atualizar_clientes(id):
    data = request.json
    cliente = ClienteService.atualizar(id, data['nome'], data['email'])
    return jsonify(cliente.to_dict()) if cliente else ('', 404)

@bp.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_clientes(id):
    ClienteService.deletar(id)
    return '', 204


#MONGODB- RElatorios

#@bp.route ("/dashboard/total_clientes",methods=["GET"])
#def dashboard_total_clientes():
   # total=obter_dashboard_total()
   # return jsonify({""})