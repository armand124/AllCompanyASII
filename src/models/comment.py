from datetime import datetime
from . import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    likes = db.Column(db.Integer, default=0)
    hearts = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Comment {self.post_id}/{self.id}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
