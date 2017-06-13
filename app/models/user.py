from app import db


class User(db.Model):
    id = db.Column(db.Integer, db.Sequence('user_id_seq'), autoincrement=True, primary_key=True)
    name = db.Column(db.String())
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    organization = db.relationship('Organization', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, name, organization):
        self.name = name
        self.organization = organization

    def __repr__(self):
        return '<User id={id} name="{name}" organization_id={organization_id}>'.format(
            id=self.id,
            name=self.name,
            organization_id=self.organization_id
        )
