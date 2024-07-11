
from flask import Blueprint, request, jsonify
from controller.book_controller import BookController

books_blueprint = Blueprint('books', __name__)
controller = BookController()

@books_blueprint.route('/books', methods=['GET'])
def get_books():
    nome = request.args.get('nome')
    if nome:
        result = controller.get(nome)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Book not found'}), 404
    return jsonify(controller.get()), 200

@books_blueprint.route('/books', methods=['POST'])
def create_book():
    data = request.json
    result = controller.create(data)
    return jsonify(result), 201

@books_blueprint.route('/books/<nome>', methods=['PUT'])
def update_book(nome):
    data = request.json
    result = controller.update(nome, data)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

@books_blueprint.route('/books/<nome>', methods=['DELETE'])
def delete_book(nome):
    result = controller.delete(nome)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Book not found'}), 404
