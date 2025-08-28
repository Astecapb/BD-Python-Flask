from flask import Blueprint, jsonify
from app.services.sql_service import ClienteService
from app.services.nosqlservice import NoSQLService

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard/total-clientes', methods=['GET'])
def total_clientes():
    total = ClienteService.contar()
    nosql = NoSQLService()
    nosql.salvar_total_clientes(total)
    return jsonify({'total_clientes': nosql.buscar_total_clientes()})