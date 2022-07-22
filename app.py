from flask import Flask, jsonify, request

app = Flask(__name__) #incializa a aplicação

#criar uma lista com dicionário e lojas e itens
lojas = [
    {
        'name':'Magazine',
        'items':[
            {
                'name': 'Jaqueta',
                'price': 300
            }
        ]
    }
]

#post  /loja/ data: {name :} - cria uma nova loja
@app.route('/loja', methods=['POST'])
def cria_loja():
    request_data = request.get_json() # reuest_data vai receber dados da request PUT /loja
    new_loja = {
        'name': request_data['name'],
        'items':[] #item não recebe nada
    }
    lojas.append(new_loja) #salva a nova loja em lojas
    return jsonify(new_loja) #precisa usar uma string por isso usamos o jsonify

#get /loja/<string:name> - retornar nossa loja
@app.route('/loja/<string:name>')
def get_loja(name):
    for loja in lojas:
        if loja['name'] == name:
            return jsonify(loja)
    return jsonify({'message': 'Loja não encontrada'})

#get \loja - retorna a lista de lojas
@app.route('/loja')
def get_lojas():
    return jsonify({'lojas': lojas})

#post /loja/<name> data:{name:, price:} - cria um item da loja
@app.route('/loja/<string:name>/item', methods=['POST'])
def cria_item_na_loja(name):
    request_data = request.get_json()
    for loja in lojas:
        if loja['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            loja=['items'].append(new_item) #salva item 
            return jsonify(new_item)
    return jsonify({'message' : 'Loja não encontrada'})

#get /loja/<nome>/item data : {name :} - pega item da loja específica
@app.route('/loja/<string:name>/item')
def get_item_na_loja(name):
    for loja in lojas:#busca se loja existe
        if loja['name'] ==name: #compara nome das lojas
            return jsonify({'items' : loja['items']})
    return jsonify({'message': 'Loja não encontrada!'})

app.run()