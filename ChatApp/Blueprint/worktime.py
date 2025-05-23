from flask import Blueprint, session, redirect, url_for, render_template, flash, request
from ChatApp.models import Worktime, User, Team

worktime_bp = Blueprint('worktime', __name__, url_prefix='/worktime')

#@app.route ではなく、 @worktime_bp.route を使用

# 勤怠の入力
@worktime_bp.route('/<int:team_id>/<int:user_id>/input', methods=['POST'])
def worktime_input(team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))
    
    start_hour = request.form.get('start_hour')
    start_minute = request.form.get('start_minute')
    end_hour = request.form.get('end_hout')
    end_minute = request.form.get('end_minute')


    worktime = Worktime.find_by_user_id(uid)

    if worktime is None:
        Worktime.create(uid, start_hour, start_minute, end_hour, end_minute)
        return redirect(url_for('channels.channels_view', team_id=team_id))
    else:
        Worktime.update(uid, start_hour, start_minute, end_hour, end_minute)
        return redirect(url_for('channels.channels_view', team_id=team_id))

# 勤怠の表示
@worktime_bp.route('/<int:team_id>/view', methods=['GET'])
def worktime_view(team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))
    
    worktimes = Worktime.get_by_team_id(team_id)

    return render_template('worktime_view.html', worktimes = worktimes, team_id = team_id)
    
    
    