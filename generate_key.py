from flask import Flask, jsonify
import secrets

app = Flask(__name__)

# Função para gerar a chave
def generate_key():
    return secrets.token_hex(16)  # Gera uma chave de 32 caracteres hexadecimais

# Rota para gerar e retornar a chave
@app.route('/generate_key', methods=['GET'])
def get_key():
    key = generate_key()
    return jsonify({"key": key}), 200

if __name__ == '__main__':
    app.run(debug=True)
