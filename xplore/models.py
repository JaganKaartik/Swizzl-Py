from xplore import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.password}')"

class GNews(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	link = db.Column(db.String(100), nullable=False)
	pubDate = db.Column(db.String(50), nullable=False)
	content = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"News('{self.title}','{self.link}','{self.pubDate}','{self.content}')"
"""
class NYNews(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	link = db.Column(db.String(100), nullable=False)
	pubDate = db.Column(db.String(50), nullable=False)
	content = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"News('{self.title}','{self.link}','{self.pubDate}','{self.content}')"
"""