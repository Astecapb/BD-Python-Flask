from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pymongo import MongoClient
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    mongo_client = MongoClient(Config.MONGO_URI)
    app.mongo_db = mongo_client[Config.MONGO_DB]

    # Importar blueprints **DEPOIS** de inicializar db
    from app.routes.clientes import bp as clientes_bp
    from app.routes.produtos import bp as produtos_bp
    from app.routes.vendas import bp as vendas_bp
    from app.routes.dashboard import bp as dashboard_bp

    app.register_blueprint(clientes_bp, url_prefix='/api')
    app.register_blueprint(produtos_bp, url_prefix='/api')
    app.register_blueprint(vendas_bp, url_prefix='/api')
    app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')


    return app