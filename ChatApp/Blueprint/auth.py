from flask import Blueprint, session, redirect, url_for, render_template, request, flash
from ChatApp.models import User, Team
import hashlib

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# サインアップページの表示

@auth_bp.route('/signup', methods=['GET'])
def signup_page():
    teams = Team.get_all_teams()  # ←ここで呼び出してる！！
    return render_template('signup.html', teams=teams)


# サインアップ処理
@auth_bp.route('/signup', methods=['POST'])
def signup_process():
    username = request.form['username']
    password = request.form['password']
    passwordConfirmation = request.form['passwordConfirmation']
    team_id = request.form['team_id']

    if username == '' or password == '' or passwordConfirmation == '' or team_id == '':
        flash('空のフォームがあります')
    elif password != passwordConfirmation:
        flash('パスワードが一致しません')
    else:
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        registered_user = User.find_by_username(username)

        if registered_user:
            flash('ユーザー名はすでに使用されています')
        else:
            User.create(username, password, team_id)
            session['user_id'] = User.find_by_username(username)['id']
            print(f"サインアップ完了")
            return redirect(url_for('auth.login_page'))

    return redirect(url_for('auth.signup_page'))

# ログインページの表示
@auth_bp.route('/login', methods=['GET'])
def login_page():
    print(f'ログインページの表示')
    return render_template('login.html')

# ログイン処理
@auth_bp.route('/login', methods=['POST'])
def login_process():
    username = request.form['username']
    password = request.form['password']

    if username == '' or password == '':
        flash('空のフォームがあります')
        return redirect(url_for('auth.login_page'))

    user = User.find_by_username(username)

    if not user:
        flash('ユーザーが存在しません')
        return redirect(url_for('auth.login_page'))

    hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if hashPassword != user['password_hash']:
        flash('パスワードが一致しません')
        return redirect(url_for('auth.login_page'))

    session['user_id'] = user['id']
    team_id = user['team_id']
    print(f"ログイン完了")
    return redirect(url_for('channels.channels_view', team_id=team_id))
