from flask import Blueprint, request
from flask import jsonify

from ..resources.reviewer_resource import ReviewerResource
from ..services import reviewer_service

blueprint = Blueprint('restaurant', __name__, url_prefix='/restaurants')

# defines GET endpoint for retrieving all reviewers
@blueprint.route('/', methods=['GET'], strict_slashes=False)
def get_reviewers():
    # restaurant_service does the actually fetching of restaurants
    result = reviewer_service.get_reviewers()
    # HTTP status code 200 means OK
    return jsonify(result), 200

# defines GET endpoint for retrieving a single reviewer based on a provided id
@blueprint.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_restaurant(id):
    result = reviewer_service.get_reviewer(id)
    if result is None:
        error = {'error': 'restaurant not found'}
        # HTTP status code 404 means Not Found
        return jsonify(error), 404

    # HTTP status code 200 means OK
    return jsonify(result), 200

@blueprint.route('/reviewers', methods=['POST'], strict_slashes=False)
def create_reviewer():
    try:
        body = ReviewerResource(**request.json)
    except Exception as error:
        return jsonify({'error': str(error)}), 400

    result = reviewer_service.create_reviewer(body.dict)
    return jsonify(result), 201

@blueprint.route("/<int:id>", methods=["DELETE"], strict_slashes=False) 
def delete_reviewer(id):     
    result = reviewer_service.delete_reviewer(id)      
    if result is None:         
        error = {"error": "reviewer not found"}         
        return jsonify(error), 404      
    return jsonify({"message": "reviewer deleted successfully"}), 200

@blueprint.route('/reviewers/<int:id>', methods=['PUT'], strict_slashes=False)
def update_reviewer(id):
    try:
        body = ReviewerResource(**request.json)
    except Exception as error:
        return jsonify({'error': str(error)}), 400

    result = reviewer_service.update_reviewer(id, body.dict)
    if result is None:
        return jsonify({'error': 'reviewer not found'}), 404

    return jsonify(result), 200