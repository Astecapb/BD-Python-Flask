from flask import Blueprint, request, jsonify # type: ignore
from app.services.sql_service import VendaService
from app.services.sql_service import ProdutoService  # para validar estoque
from app import db

bp = Blueprint('vendas', __name__)

# Criar nova venda
@bp.route('/vendas', methods=['POST'])
def criar():
    data = request.json

    # validação básica de campos
    required = ['id_cliente', 'produto_id', 'quantidade', 'valor_total']
    if not all(k in data for k in required):
        return {'error': 'Campos obrigatórios faltando'}, 400

    venda = VendaService.criar(
        id_cliente=int(data['id_cliente']),
        produto_id=int(data['produto_id']),
        quantidade=int(data['quantidade']),
        valor_total=float(data['valor_total'])
    )
    return jsonify(venda.to_dict()), 201


# Listar todas as vendas
@bp.route('/vendas', methods=['GET'])
def listar():
    vendas = VendaService.listar()
    return jsonify([v.to_dict() for v in vendas]), 200


# Buscar venda por ID
@bp.route('/vendas/<int:id>', methods=['GET'])
def buscar(id):
    venda = VendaService.buscar(id)
    if not venda:
        return {'error': 'Venda não encontrada'}, 404
    return jsonify(venda.to_dict()), 200


# Atualizar venda
@bp.route('/vendas/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.json
    venda = VendaService.atualizar(
        id,
        id_cliente=int(data['id_cliente']),
        produto_id=int(data['produto_id']),
        quantidade=int(data['quantidade']),
        valor_total=float(data['valor_total'])
    )
    if not venda:
        return {'error': 'Venda não encontrada'}, 404
    return jsonify(venda.to_dict()), 200


# Deletar venda
@bp.route('/vendas/<int:id>', methods=['DELETE'])
def deletar(id):
    VendaService.deletar(id)
    return '', 204