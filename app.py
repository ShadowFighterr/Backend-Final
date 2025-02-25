import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from config import Config
from models import db, Task, User
from flask_migrate import Migrate
from forms import RegistrationForm, LoginForm, DeleteAccountForm, ChangePasswordForm
from flask_login import login_required, LoginManager, login_user, current_user, logout_user
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create tables
#with app.app_context():
#    print("Creating tables...")
#    db.create_all()
#    print("Tables created.")

# Welcome page for unauthenticated users
@app.route('/')
def index():
    if current_user.is_authenticated:
        tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
        return render_template('index.html', tasks=tasks)
    else:
        return render_template('welcome.html')

@app.route('/add', methods=['POST'])
@login_required
def add_task():
    title = request.form['title']
    info = request.form.get('info')
    due_date = request.form.get('due_date')
    new_task = Task(title=title, info=info, due_date=due_date, user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("You are not authorized to delete this task.", "danger")
        return redirect(url_for('index'))
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_status/<int:id>', methods=['POST'])
@login_required
def update_status(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        return jsonify({'result': 'error', 'message': 'Unauthorized'}), 403
    new_status = request.form.get('status')
    task.status = new_status
    db.session.commit()
    return jsonify({'result': 'success'})

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("You are not authorized to edit this task.", "danger")
        return redirect(url_for('index'))
    if request.method == 'POST':
        task.title = request.form['title']
        task.info = request.form['info']
        task.due_date = request.form.get('due_date')
        task.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already taken!', 'danger')
            return redirect(url_for('register'))

        try:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash("Registration failed. Please try again.", 'danger')
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    delete_form = DeleteAccountForm()
    password_form = ChangePasswordForm()
    
    if password_form.validate_on_submit():
        if current_user.check_password(password_form.current_password.data):
            current_user.set_password(password_form.new_password.data)
            db.session.commit()
            flash('Password updated successfully!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Incorrect current password', 'danger')
    
    return render_template('profile.html',
                         user=current_user,
                         delete_form=delete_form,
                         password_form=password_form)

@app.route('/demo')
def demo():
    demo_user = User.query.filter_by(email="demo@example.com").first()
    if not demo_user:
        demo_user = User(username="DemoUser", email="demo@example.com")
        demo_user.set_password("demo")
        db.session.add(demo_user)
        db.session.commit()
    login_user(demo_user)
    flash("Logged in as demo user.", "success")
    return redirect(url_for('index'))

@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    form = DeleteAccountForm()
    if form.validate_on_submit():
        Task.query.filter_by(user_id=current_user.id).delete()
        User.query.filter_by(id=current_user.id).delete()
        db.session.commit()
        logout_user()
        flash('Account deleted successfully', 'success')
        return redirect(url_for('index'))
    flash('Invalid request', 'danger')
    return redirect(url_for('profile'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
