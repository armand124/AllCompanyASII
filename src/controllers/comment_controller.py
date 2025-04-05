from flask import jsonify, request
from models import Comment, db

def add_comment(_post_id):
    try:
        data = request.get_json()
        content = data.get("content")
        if not content:
            return "You can't post an empty comment", 400
        if not _post_id:
            return "Error, post not found", 404
        comment = Comment(post_id=_post_id, content=data['content'])
        comment.save()

        return jsonify({
            'id': comment.id,
            'post_id': comment.post_id,
            'content': comment.content,
            'likes': comment.likes,
            'hearts': comment.hearts,
            'created_at': comment.created_at
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message" : str(e)}), 500

def get_comment_by_id(comment_id):
    comment = db.session.get(Comment,comment_id)
    if comment:
        return jsonify({
            'id': comment.id,
            'post_id': comment.post_id,
            'content': comment.content,
            'likes': comment.likes,
            'hearts': comment.hearts,
            'created_at': comment.created_at
        }), 200
    else:
        return jsonify({'message' : 'Comment not found'}), 404

def get_comments_by_post_id(_post_id):
    comments = Comment.query.filter_by(post_id=_post_id).all()
    result = []
    print(comments)
    if comments:
        for comment in comments:
            result.append({
                'id':comment.id,
                'post_id': comment.post_id,
                'content': comment.content,
                'likes': comment.likes,
                'hearts': comment.hearts,
                'created_at': comment.created_at
            })
        return jsonify(result), 200
    else:
        return jsonify({'message' : 'The post does not have any comments'}), 404

def like_comment(comment_id):
    comment = db.session.get(Comment,comment_id)

    if not comment:
        return jsonify({'message' : 'Comment not found'}), 404

    comment.likes += 1
    comment.save()
    return jsonify({"message" : f"Comment liked. Now the comment has : {comment.likes} likes."})

def delete_comment(comment_id):
    comment = db.session.get(Comment,comment_id)
    if not comment:
        return jsonify({'message' : 'Comment not found'}), 404
    else:
        db.session.delete(comment)
        db.session.commit()
        return jsonify({'message' : f'Comment deleted {comment.content}'}), 200