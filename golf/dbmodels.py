from golf import db
class game(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    player_name = db.Column(db.String(length=40), nullable=False)
    hole = db.Column(db.Integer(), nullable=False)
    score = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'item {self.name}'