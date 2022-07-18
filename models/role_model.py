from extensions import db

class Role(db.Model):
    __tablename__ = "role"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    