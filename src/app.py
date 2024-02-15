from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/myroute', methods=['GET'])
def hello_world():
    json_text = jsonify(some_data)
    return json_text

@app.route('/todos', methods=['GET'])
def handle_todos():
    return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos [position]
    return todos

some_data = { "name": "Bobby", "lastname": "Rixer" }

# lista [] con dizionario {} dentro, Python
# Array [] con objetos {} dentr , Javascript
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)