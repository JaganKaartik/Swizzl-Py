from xplore.models import User

admin.add_view(ModelView(User, db.session))