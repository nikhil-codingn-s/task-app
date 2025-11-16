from flask import Flask, jsonify, request
from uuid import uuid4

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return jsonify({"status": "ok", "tasks": len(tasks)})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() or {}
    task = {
        'id': str(uuid4()),
        'title': data.get('title', 'Untitled'),
        'done': False
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json() or {}
    for t in tasks:
        if t['id'] == task_id:
            t['title'] = data.get('title', t['title'])
            t['done'] = data.get('done', t['done'])
            return jsonify(t)
    return jsonify({"error": "not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

