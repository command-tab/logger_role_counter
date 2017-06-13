from app import db


class Organization(db.Model):
    id = db.Column(db.Integer, db.Sequence('organization_id_seq'), autoincrement=True, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Organization id={id} name="{name}">'.format(
            id=self.id,
            name=self.name
        )
