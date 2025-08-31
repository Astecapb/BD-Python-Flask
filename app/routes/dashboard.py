from flask import Blueprint, jsonify
import app
from sql_service2 import ClienteService
from app.services.nosqlservice import NoSQLService

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard/total-clientes', methods=['GET'])
def total_clientes():
    total = ClienteService.contar()
    nosql = NoSQLService()
    nosql.salvar_total_clientes(total)
    return jsonify({'total_clientes': nosql.buscar_total_clientes()})

@bp.route('/', methods=['GET'])
def dashboard():
    ns = NoSQLService()
    ns.atualizar_dashboard()
    return jsonify(ns.obter_dashboard())

def obter_dashboard(self):
        return self.col.find_one({'_id': 'dashboard'})

if __name__ == "__main__":
    app.run(debug=True)