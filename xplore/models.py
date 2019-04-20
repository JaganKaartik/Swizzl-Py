from xplore import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.password}')"

class News(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	link = db.Column(db.String(100), nullable=False)
	pubDate = db.Column(db.String(50), nullable=False)
	content = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"Post('{self.title}','{self.link}','{self.pubDate}','{self.content}')"
