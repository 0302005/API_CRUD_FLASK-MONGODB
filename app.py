from flask import Flask, request, jsonify
from pymongo import MongoClient
from mongopass import mongopass

app = Flask(__name__)
app.config["DEBUG"] = True

# conexão com o banco de dados
client = MongoClient(mongopass)
db = client.get_database('Flask+MongoDB')   # nome do banco
minhacolecao = db.get_collection('produtos')   # nome da coleção


# Consultar (todos)
@app.route('/produtos', methods=['GET'])
def obter_produtos():
    produtos = minhacolecao.find()

    return jsonify([produto for produto in produtos])


# Consultar (id)
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto_por_id(id):
    produto = minhacolecao.find_one({"_id": id})

    return produto


# Editar
@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_produto_por_id(id):
    prod_alt = request.get_json()
    produto_alterado = minhacolecao.find_one_and_update(
        {'_id': id},
        {'$set': {'preco': prod_alt['preco']}}
        )

    return produto_alterado


# Criar
@app.route('/produtos', methods=['POST'])
def incluir_novo_produto():
    novo_produto = request.get_json()
    minhacolecao.insert_one(novo_produto)

    return jsonify(message="adicionado com sucesso")


# Excluir
@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    minhacolecao.delete_one({'_id': id})

    return jsonify(message="removido com sucesso")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
