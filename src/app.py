from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    todos_text= jsonify(todos)
    return todos_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    todos_list= jsonify(todos)
    return todos_list

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    todos_list=jsonify(todos)
    return todos_list














if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)