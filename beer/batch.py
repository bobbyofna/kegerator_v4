import base64

import pytz
from datetime import datetime

import requests as requests

from beer import db

class Batch(db.Model):
    __tablename__ = 'batch'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    _id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), default='')
    #keg_id = db.Column(db.Integer, db.ForeignKey('keg.id'))
    style = db.Column(db.String(128), nullable=False)
    #votes = db.relationship('Vote', backref='batch', order_by="desc(Vote.timestamp)", lazy='dynamic')

    gas = db.Column(db.String(64), default='CO2')
    volume = db.Column(db.Float, default=5.0)
    brew_date = db.Column(db.DateTime, nullable=False)
    finish_date = db.Column(db.DateTime, nullable=False)
    kegged = db.Column(db.Boolean, default=False)

    abv = db.Column(db.Float, nullable=False)
    ibu = db.Column(db.Float, nullable=False)
    og = db.Column(db.Float, nullable=False)
    fg = db.Column(db.Float, nullable=False)
    srm = db.Column(db.Float, nullable=False)
    kcal = db.Column(db.Float, nullable=False)
    malts = db.Column(db.PickleType(), default=[], nullable=False)
    hops = db.Column(db.PickleType(), default=[], nullable=False)
    yeast = db.Column(db.PickleType(), default=[], nullable=False)

    def __init__(self, _id, _name, _style, _brew_date, _finish_date, _abv, _ibu, _og, _fg, _srm, _kcal, _malts, _hops, _yeast, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.name = _name
        self.style = _style
        self.brew_date = _brew_date
        self.finish_date = _finish_date
        self.abv = _abv
        self.ibu = _ibu
        self.og = _og
        self.fg = _fg
        self.srm = _srm
        self.kcal = _kcal
        self.malts = _malts
        self.hops = _hops
        self.yeast = _yeast
        print("SUCCESSFULLY CREATED A BATCH")

    #PROPERTIES
    #age
    #kicked
    #overall_rating
    #reviewers

    @staticmethod
    def existCheck(_id):
        try:
            batches = db.session.query(Batch).all()
            for batch in batches:
                if batch._id == _id:
                    return True
        except Exception as e:
            return False
        return False

    @staticmethod
    def getBatches():
        us = 'ZssoJ8xEdPSgJZ6anvFHY9fuXXr1'
        pw = 'J7WQ9sV0Vl7COiiB8z4pt27dPfGIrM9MOVmUqgxz223HOlTnFJTnhjEBySebV0B7'
        #b64 = base64.b64encode(bytes(:, 'utf-8'))
        _resp = requests.get(url='https://api.brewfather.app/v1/batches', auth=(us, pw), params={'complete': True, 'limit': 50})
        _json = _resp.json()
        #print(_json)
        for batch in _json:
            _id = int(batch['batchNo'])
            if Batch.existCheck(_id) == False:
                tz = pytz.timezone('America/New_York')
                _name = '{}'.format(batch['recipe']['name'])
                _brew_date = datetime.fromtimestamp(int(batch['brewDate']) / 1000.0, tz=tz)
                _finish_date = datetime.fromtimestamp(int(batch['bottlingDate']) / 1000.0, tz=tz)
                _abv = float(batch['measuredAbv'])
                _ibu = float(batch['estimatedIbu'])
                _srm = float(batch['estimatedColor'])
                _og = float(batch['estimatedOg'])
                _fg = float(batch['estimatedFg'])
                _kcal = float(batch['recipe']['nutrition']['calories']['kJ'])
                _style = ''
                try:
                    #_style = '{}'.format(batch['recipe']['style']['name'])
                    _style = ''
                except:
                    _style = ''
                _hops = []
                _yeast = []
                _malts = []
                for hop in batch['batchHops']:
                    _hops.append('{}'.format(hop['name']))
                for yest in batch['batchYeasts']:
                    _yeast.append('{}'.format(yest['name']))
                for malt in batch['batchFermentables']:
                    _malts.append('{}'.format(malt['name']))

                _batch = Batch(_id, _name, _style, _brew_date, _finish_date, _abv, _ibu, _og, _fg, _srm, _kcal, _malts, _hops, _yeast)
                db.session.add(_batch)

        return _json
