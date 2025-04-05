from flask import Blueprint
from controllers.comment_controller import *

comment_routes = Blueprint('comments_routes', __name__)

@comment_routes.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    return add_comment(post_id)

@comment_routes.route('/posts/<int:post_id>/comments', methods=['GET'])
def list_comments(post_id):
    return get_comments_by_post_id(post_id)

@comment_routes.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    return get_comment_by_id(comment_id)

@comment_routes.route('/comments/<int:comment_id>', methods=['POST'])
def like_comment_by_id(comment_id):
    return like_comment(comment_id)

@comment_routes.route('/comments/<int:comment_id>', methods=['DELETE'])
def del_comment(comment_id):
    return delete_comment(comment_id)


