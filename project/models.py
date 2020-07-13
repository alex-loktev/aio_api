from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    avatar_url = db.Column(db.String())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'params': self.avatar_url,
        }


