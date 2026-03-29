from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Food
from ..extensions import db
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add')
def add_food():
    foods = Food.query.all()
    return render_template('add.html', foods=foods)

@main.route('/add', methods=['POST'])
def add_food_post():
    food_name = request.form.get('food_name')
    proteins = request.form.get('proteins')
    carbs = request.form.get('carbohydrates')
    fats = request.form.get('fats')
    new_food = Food(name=food_name, proteins=proteins, carbs=carbs, fats=fats)
    
    db.session.add(new_food)
    db.session.commit()
    
    return redirect(url_for('main.add_food'))


@main.route('/delete_food/<int:food_id>', methods=['POST'])
def delete_food(food_id):
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    return redirect(url_for('main.add_food'))


@main.route('/edit_food/<int:food_id>', methods=['POST'])
def edit_food(food_id):
    food = Food.query.get_or_404(food_id)
    food.name = request.form.get('food_name')
    food.proteins = request.form.get('proteins')
    food.carbs = request.form.get('carbohydrates')
    food.fats = request.form.get('fats')
    db.session.commit()
    return redirect(url_for('main.add_food'))


@main.route('/view')
def view_food():
    foods = Food.query.all()
    return render_template('view.html', foods=foods)