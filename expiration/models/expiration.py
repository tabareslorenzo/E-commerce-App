from datetime import datetime
from datetime import timedelta

# orderID, expireTime, isSent
class expiration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderID = db.Column(db.String(80), nullable=False)
    isSent = db.Column(db.Boolean, nullable=False, default=False)
    expireTime = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow  + timedelta(seconds=60*15))

    def __repr__(self):
        return '<Expire %r>' % self.orderID