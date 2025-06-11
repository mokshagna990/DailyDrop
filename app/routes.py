# routes.py
from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.forms import RegisterForm, LoginForm, DiaryEntryForm
from app.models import User, DiaryEntry

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return redirect(url_for('main.dashboard'))

@main.route('/dashboard')
@login_required
def dashboard():
    entries = DiaryEntry.query.filter_by(author=current_user).order_by(DiaryEntry.date_posted.desc()).all()
    return render_template('dashboard.html', entries=entries)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('You have been logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')

    return render_template('login.html', title='Login', form=form)

@main.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('main.login'))

@main.route('/diary/new', methods=['GET', 'POST'])
@login_required
def new_diary_entry():
    form = DiaryEntryForm()
    if form.validate_on_submit():
        entry = DiaryEntry(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(entry)
        db.session.commit()
        flash('Your diary entry has been created!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('diary_form.html', title="New Diary Entry", form=form)

@main.route('/diary/<int:entry_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)
    if entry.author != current_user:
        flash('You do not have permission to edit this entry.', 'danger')
        return redirect(url_for('main.dashboard'))

    form = DiaryEntryForm()
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        db.session.commit()
        flash('Your diary entry has been updated!', 'success')
        return redirect(url_for('main.dashboard'))
    elif request.method == 'GET':
        form.title.data = entry.title
        form.content.data = entry.content

    return render_template('diary_form.html', title="Edit Diary Entry", form=form)

@main.route('/diary/<int:entry_id>/delete')
@login_required
def delete_entry(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)
    if entry.author != current_user:
        flash('You do not have permission to delete this entry.', 'danger')
        return redirect(url_for('main.dashboard'))

    db.session.delete(entry)
    db.session.commit()
    flash('Your diary entry has been deleted!', 'success')
    return redirect(url_for('main.dashboard'))
