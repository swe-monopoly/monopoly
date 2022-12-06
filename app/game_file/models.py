from datetime import datetime

from app import db


class GameFile(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    file = db.Column(db.LargeBinary)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    code = db.Column(db.String(125), nullable=False)
