from beer import db

class Keg(db.Model):
    __tablename__ = 'keg'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    capacity = db.Column(db.Float, default=5.0)

    #batch = db.relationship('Batch', backref='keg')
    pressure = db.Column(db.Float, default=0.0)
    temperature = db.Column(db.Float, default=36.0)
    level = db.Column(db.Float, default=0.0)

    #packets = db.relationship('Packet', backref='keg', order_by="desc(Packet.timestamp)", lazy='dynamic')
    #cal_test_cases = db.Column(db.PickleType(), default=[])
    #brewfather_url = db.Column(db.String(256), default="http://log.brewfather.net/stream?id=6Skx3cpzRKzoRZ")

    def __init__(self, _capacity=5.0, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Keg #{}'.format(self.id + 1)
        self.capacity = _capacity
        print("SUCCESSFULLY CREATED A KEG")

    def function1(self):
        hello = 1