from app import db


class GameStatistics(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BIGINT, db.ForeignKey('user.id'))
    won = db.Column(db.BIGINT)
    lost = db.Column(db.BIGINT)


