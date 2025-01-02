from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Task

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# create tables
with app.app_context():
    print("Creating tables...")
    db.create_all()
    print("Tables created.")

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)