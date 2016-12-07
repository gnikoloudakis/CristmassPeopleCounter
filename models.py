from ChristmasPeopleCounter import db


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people = db.Column(db.Integer)

    def __init__(self, count):
        self.count = count

    def __repr__(self):
        return '<People Count is: %r>' % self.count
