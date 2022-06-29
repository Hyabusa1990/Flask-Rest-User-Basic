from extensions import db
from passlib.hash import pbkdf2_sha256


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    @property
    def data(self):
        return {
            'id': self.id,
            'username': self.username
        }

    @property
    def Username(self):
        return self.username

    @Username.setter
    def Username(self, value):
        self.username = value or self.username

    @property
    def Password(self):
        return self.password

    @Password.setter
    def Password(self, value):
        if value:
            self.password = self.hash_password(value)

    @classmethod
    def hash_password(cls, password):
        return pbkdf2_sha256.hash(password)

    @classmethod
    def verify_password(cls, password, hashed):
        return pbkdf2_sha256.verify(password, hashed)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()
