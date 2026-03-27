from flask import Blueprint, render_template, request
from foodtracker.models import Food
from foodtracker.extensions import db
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add')
def add_food():
    return render_template('add.html')

@main.route('/add', methods=['POST'])
def add_food_post():
    food_name = request.form.get('food_name')
    proteins = request.form.get('proteins')
    carbs = request.form.get('carbohydrates')
    fats = request.form.get('fats')
    new_food = Food(name=food_name, proteins=proteins, carbohydrates=carbs, fats=fats)
    return f'<h1>{food_name} - {proteins} - {carbs} - {fats}</h1>'

@main.route('/view')
def view_food():
    return render_template('view.html')