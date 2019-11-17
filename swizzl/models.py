from swizzl import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    roles = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.password}','{self.roles}')"

    def has_role(self,role):
        return role in self.roles


class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Genre = db.Column(db.String(10), nullable=False)
	title = db.Column(db.String(100), nullable=False)
	link = db.Column(db.String(100), nullable=False)
	pubDate = db.Column(db.String(50), nullable=False)
	content = db.Column(db.Text, nullable=False)


	def __repr__(self):
		return f"Posts('{self.Genre}','{self.title}','{self.link}','{self.pubDate}','{self.content}')"
