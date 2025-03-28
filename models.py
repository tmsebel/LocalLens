from __init__ import db  # Import db from __init__.py

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    restaurant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))

class Review(db.Model):
    __tablename__ = 'reviews'
    review_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))
    review_text = db.Column(db.Text)
    rating = db.Column(db.Float)
    platform = db.Column(db.String(255))

class CategorySentiment(db.Model):
    __tablename__ = 'categorysentiments'
    category_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))
    category_name = db.Column(db.String(255))
    sentiment_score = db.Column(db.Float)

class MealSentiment(db.Model):
    __tablename__ = 'mealsentiments'
    meal_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))
    meal_name = db.Column(db.String(255))
    sentiment_score = db.Column(db.Float)