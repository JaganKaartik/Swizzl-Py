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


class ViewPosts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sentid = db.Column(db.Integer, primary_key=False)
	title = db.Column(db.String(200), nullable=False)
	link = db.Column(db.String(150), nullable=False)
	linkdata = db.Column(db.String(2000), nullable=False)
	tbscore = db.Column(db.String(50),nullable=False)
	vaderscorePos = db.Column(db.String(50),nullable=False)
	vaderscoreNeut = db.Column(db.String(50),nullable=False)
	vaderscoreNeg = db.Column(db.String(50),nullable=False)
	vaderscoreComp = db.Column(db.String(20),nullable=False)
	prof = db.Column(db.String(50),nullable=False)
	pubDate = db.Column(db.String(50),nullable=False)


	def __repr__(self):
		return f"ViewPosts('{self.sentid}','{self.title}','{self.link}','{self.linkdata}','{self.tbscore}','{self.vaderscorePos}',{self.vaderscoreNeut}',{self.vaderscoreNeg}','{self.vaderscoreComp}','{self.prof}','{self.pubDate}')"
