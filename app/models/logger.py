from app import db


class Logger(db.Model):
    id = db.Column(db.Integer, db.Sequence('logger_id_seq'), autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('loggers', lazy='dynamic'))
    logger_role_id = db.Column(db.Integer, db.ForeignKey('logger_role.id'))
    logger_role = db.relationship('LoggerRole', backref=db.backref('loggers', lazy='dynamic'))

    def __init__(self, user, logger_role):
        self.user = user
        self.logger_role = logger_role

    def __repr__(self):
        return '<Logger id={id} user_id={user_id} logger_role_id={logger_role_id}>'.format(
            id=self.id,
            user_id=self.user_id,
            logger_role_id=self.logger_role_id
        )
