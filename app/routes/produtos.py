from flask import Blueprint, request, jsonify # type: ignore
from app.services.sql_service import ProdutoService

bp = Blueprint('produtos', __name__)

@bp.route('/produtos', methods=['POST'])
def criar():
    data = request.json
    produto = ProdutoService.criar(
        data['nome'],
        float(data['preco']),
        int(data.get('estoque', 0))
    )
    return jsonify(produto.to_dict()), 201

@bp.route('/produtos', methods=['GET'])
def listar():
    produtos = ProdutoService.listar()
    return jsonify([p.to_dict() for p in produtos])

@bp.route('/produtos/<int:id>', methods=['GET'])
def buscar(id):
    produto = ProdutoService.buscar(id)
    return jsonify(produto.to_dict()) if produto else ('', 404)

@bp.route('/produtos/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.json
    produto = ProdutoService.atualizar(
        id,
        data['nome'],
        float(data['preco']),
        int(data.get('estoque', 0))
    )
    return jsonify(produto.to_dict()) if produto else ('', 404)

@bp.route('/produtos/<int:id>', methods=['DELETE'])
def deletar(id):
    ProdutoService.deletar(id)
    return '', 204