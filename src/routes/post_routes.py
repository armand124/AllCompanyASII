from flask import Blueprint
from controllers.post_controller import *

from controllers.comment_controller import get_comments_by_post_id

posts_routes = Blueprint("posts_routes", __name__)


@posts_routes.route('/', methods=['GET'])
def index():
    return jsonify("Hello, Pog")


@posts_routes.route('/posts', methods=['POST'])
def create_post():
    return add_post()


@posts_routes.route('/posts', methods=['GET'])
def list_posts():
    return get_posts()

@posts_routes.route('/posts/<int:post_id>', methods=['GET'])
def list_post_by_id(post_id):
    return get_post_by_id(post_id)


@posts_routes.route('/posts/<int:post_id>/like', methods=['POST'])
def create_like(post_id):
    return like_post(post_id)


@posts_routes.route('/posts/<int:post_id>/likes', methods=['GET'])
def list_likes(post_id):
    return get_likes(post_id)


@posts_routes.route('/posts/<int:post_id>/heart', methods=['POST'])
def create_heart(post_id):
    return love_post(post_id)


@posts_routes.route('/posts/<int:post_id>/hearts', methods=['GET'])
def list_hearts(post_id):
    return get_hearts(post_id)
