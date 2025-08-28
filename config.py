import os

class Config:
    # PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:post1234@localhost:5432/dbpos'

    #SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:post1234@localhost:5432/bdpos"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MongoDB
    MONGO_URI = "mongodb://localhost:27017/"
    MONGO_DB = "vendas"
    MONGO_COLLECTION="clientes"
