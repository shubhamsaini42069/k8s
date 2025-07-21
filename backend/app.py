from flask import Flask, jsonify
from connections import collections
import os
app = Flask(__name__)
PORT=os.environ.get('PORT', 5000)
@app.route('/')
def index():
    return jsonify({
        'message': 'backend running successfully',
        'status': 'success'})



@app.route('/api/get')
def api():
    names=collections.find()

    result = []
    for name in names:

        result.append(name['value'])

    result={'names': result}

    return jsonify(result)
    
@app.route('/api/add/<name>')
def add_name(name):
    collections.insert_one({'value': name})
    return jsonify({'message': f'Name {name} added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)