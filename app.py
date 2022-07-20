from cProfile import run
from flask import Flask, jsonify

app = Flask(__name__) #incializa a aplicação

#criar uma lista com dicionário e lojas e itens
lojas = [
    {
        'name':'Magazine',
        'itens':[
            {
                'name': 'Jaqueta',
                'price': 300
            }
        ]
    }
]

#post  /loja/ data: {name :} - cria uma nova loja
@app.route(' /loja', methods=['POST'])
def cria_loja():
    pass

@app.route(' /loja')
def get_lojas():
    return jsonify({'lojas': lojas})

app(run)