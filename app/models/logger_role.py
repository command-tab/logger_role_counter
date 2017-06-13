from app import db


class LoggerRole(db.Model):
    id = db.Column(db.Integer, db.Sequence('logger_role_id_seq'), autoincrement=True, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<LoggerRole id={id} name="{name}">'.format(
            id=self.id,
            name=self.name
        )
