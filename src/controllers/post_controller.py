from flask import jsonify, request
from models import Post, db, Comment
def add_post():
    try:
        data = request.get_json()

        content = data.get("content")
        if not content:
            return "Content cannot be empty", 400
        if len(content) < 10:
            return "Content must be at least 10 characters long.", 400

        post = Post(content=data["content"])
        post.save()

        return jsonify({
            'id': post.id,
            'content': post.content,
            'likes': post.likes,
            'hearts': post.hearts,
            'created_at': post.created_at
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500


def get_post_by_id(post_id):
    post = db.session.get(Post, post_id)
    if post:
        return jsonify({
            'id': post.id,
            'content': post.content,
            'likes': post.likes,
            'hearts': post.hearts,
            'created_at': post.created_at
        }), 200
    else:
        return jsonify({'message': 'Post not found'}), 404


def get_posts():
    posts = Post.query.all()
    if not posts:
        return jsonify({"message": "No posts found"}), 404

    result = []
    for post in posts:
        result.append({
            "id": post.id,
            "content": post.content,
            "likes": post.likes,
            "hearts": post.hearts,
            "created_at": post.created_at
        })
    return jsonify(result), 200

def delete_post(_post_id):
    post = db.session.get(Post, _post_id)
    if post:
        comments = Comment.query.filter_by(post_id=_post_id).all()
        for comment in comments:
            db.session.delete(comment)
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Post deleted'}), 200

def like_post(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404

    post.likes += 1
    post.save()
    return jsonify({"message": "You reacted with a like", "likes": post.likes})


def get_likes(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404
    return jsonify({"likes": post.likes})


def love_post(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404

    post.hearts += 1
    post.save()

    return jsonify({"message": "You reacted with a heart", "hearts": post.hearts})


def get_hearts(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404
    return jsonify({"hearts": post.hearts})
