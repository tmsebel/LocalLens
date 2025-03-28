from flask import Flask, jsonify, request
from __init__ import db #Import db from __init__.py
import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Simon%401954@127.0.0.1/beryldb'

@app.route('/restaurants/search', methods=['GET'])
def search_restaurants():
    query = request.args.get('query')
    if query:
        restaurants = models.Restaurant.query.filter(models.Restaurant.name.like(f'%{query}%')).all()
    else:
        restaurants = models.Restaurant.query.all()
    results = [{'restaurant_id': r.restaurant_id, 'name': r.name, 'address': r.address} for r in restaurants]
    return jsonify(results)

@app.route('/restaurants/<int:restaurant_id>/reviews', methods=['GET'])
def get_restaurant_reviews(restaurant_id):
    restaurant = models.Restaurant.query.get(restaurant_id)
    if restaurant:
        reviews = models.Review.query.filter_by(restaurant_id=restaurant_id).all()
        results = [{'review_id': r.review_id, 'review_text': r.review_text, 'rating': r.rating, 'platform': r.platform} for r in reviews]
        return jsonify(results)
    else:
        return jsonify({'message': 'Restaurant not found'}), 404

@app.route('/restaurants/<int:restaurant_id>/categories', methods=['GET'])
def get_restaurant_categories(restaurant_id):
    restaurant = models.Restaurant.query.get(restaurant_id)
    if restaurant:
        categories = models.CategorySentiment.query.filter_by(restaurant_id=restaurant_id).all()
        results = [{'category_name': c.category_name, 'sentiment_score': c.sentiment_score} for c in categories]
        return jsonify(results)
    else:
        return jsonify({'message': 'Restaurant not found'}), 404

@app.route('/restaurants/<int:restaurant_id>/meals', methods=['GET'])
def get_restaurant_meals(restaurant_id):
    restaurant = models.Restaurant.query.get(restaurant_id)
    if restaurant:
        meals = models.MealSentiment.query.filter_by(restaurant_id=restaurant_id).all()
        results = [{'meal_name': m.meal_name, 'sentiment_score': m.sentiment_score} for m in meals]
        return jsonify(results)
    else:
        return jsonify({'message': 'Restaurant not found'}), 404

if __name__ == '__main__':
    db.init_app(app) #Add this line
    app.run(debug=True, port=5001)