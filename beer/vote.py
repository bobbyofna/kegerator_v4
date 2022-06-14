from datetime import datetime
from beer import db

class Vote(db.Model):
    __tablename__ = 'vote'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    #batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'))
    name = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())

    overall = db.Column(db.Float, nullable=False)
    taste = db.Column(db.Float, default=None)
    mouthfeel = db.Column(db.Float, default=None)
    body = db.Column(db.Float, default=None)
    flavors = db.Column(db.String(256), default='')
    comments = db.Column(db.String(1024), default='')

    def __init__(self, _name, _overall, **kwargs):
        super().__init__(**kwargs)
        self.name = _name
        self.overall = _overall
        print("SOMEONE SUCCESSFULLY VOTED")