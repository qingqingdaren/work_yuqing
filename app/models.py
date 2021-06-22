from . import db


class Cucnews(db.Model):
    __tablename__ = 'cucnews'
    id = db.Column(db.Integer, primary_key=True)
    arti_title = db.Column(db.String(255))
    arti_from = db.Column(db.String(255))
    newstime = db.Column(db.String(255))
    arti_content = db.Column(db.String(20000))
    visit_num = db.Column(db.String(255))
    picsurl = db.Column(db.String(255))
    newsurl = db.Column(db.String(255))


class DouBan(db.Model):
    __tablename__ = 'douban'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    tags = db.Column(db.String(255))
    link = db.Column(db.String(255))
    img = db.Column(db.String(255))
    summary = db.Column(db.String(10000))

class WakeUp(db.Model):
    __tablename__ = 'wakeup'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(10000))