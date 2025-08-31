from app.services.nosqlservice import NoSQLService

# Instancia o serviço
ns = NoSQLService()

# Exibe informações básicas
print("✅ Conectado ao MongoDB em:", ns.client.address)
print("📦 Banco:", ns.db.name)
print("📁 Coleção:", ns.col.name)

# Verifica se a coleção está vazia ou não
count = ns.col.count_documents({})
print("📊 Documentos na coleção:", count)

# Opcional: tenta buscar o dashboard
dashboard = ns.obter_dashboard()
print("📋 Dashboard atual:", dashboard)