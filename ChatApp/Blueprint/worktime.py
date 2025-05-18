from flask import Blueprint, session, redirect, url_for, render_template, flash, request
from ChatApp.models import Worktime, User, Team

worktime_bp = Blueprint('worktime', __name__, url_prefix='/worktime')

#@app.route ではなく、 @worktime_bp.route を使用

# 勤怠の入力
@worktime_bp.route('/<int:team_id>', methods=['POST'])
def worktime_input(team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))

    uid = request.form.get('user_id')    
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')

    worktime = Worktime.find_by_user_id(uid)

    if worktime is None:
        Worktime.create(uid, start_time, end_time)
    else:
        Worktime.update(uid, start_time, end_time)

# 勤怠の表示
@worktime_bp.route('/<int:team_id>', methods=['GET'])
def worktime_view(team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))
    
    worktimes = Worktime.get_by_team_id(team_id)
    team_members = User.get_team_members(team_id)

    return render_template('work_time_log.html', worktimes = worktimes, team_id = team_id, team_members = team_members)
    
    
    