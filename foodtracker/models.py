from .extensions import db

log_food = db.Table('log_food',
    log_id = db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
    food_id = db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_key=True)
)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    proteins = db.Column(db.Float, nullable=False)
    carbs = db.Column(db.Float, nullable=False)
    fats = db.Column(db.Float, nullable=False)
    
    
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    foods = db.relationship('Food', secondary='log_food', backref=db.backref('logs', lazy=True))