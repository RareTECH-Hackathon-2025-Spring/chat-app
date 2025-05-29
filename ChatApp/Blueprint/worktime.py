from flask import Blueprint, session, redirect, url_for, render_template, flash, request
import re
import datetime
from ChatApp.models import Worktime, User, Team

worktime_bp = Blueprint('worktime', __name__, url_prefix='/worktime')

#@app.route ではなく、 @worktime_bp.route を使用

# 勤怠の入力
@worktime_bp.route('/<int:team_id>', methods=['POST'])
def worktime_input(team_id):
    logged_in_uid = session.get('user_id')
    if logged_in_uid is None:
        flash("ログインしてください。", "warning")
        return redirect(url_for('auth.login_page'))

    user_id_from_form = request.form.get('user_id')    
    start_time_str = request.form.get('start_time')
    end_time_str = request.form.get('end_time')

    if not user_id_from_form:
        flash("ユーザーを選択してください。", "error")
        return redirect(url_for('worktime.worktime_view', team_id=team_id))

    try:
        uid = int(user_id_from_form)
    except (ValueError, TypeError):
        flash("無効なユーザーIDです。", "error")
        return redirect(url_for('worktime.worktime_view', team_id=team_id))

    time_pattern = re.compile(r'^(?:2[0-3]|[01]?[0-9]):[0-5][0-9]$')

    start_time_obj = None
    end_time_obj = None

    if start_time_str and time_pattern.match(start_time_str):
        try:
            parts = start_time_str.split(':')
            start_time_obj = datetime.time(hour=int(parts[0]), minute=int(parts[1]), second=0)
        except ValueError as e:
            flash(f"開始時間の変換に失敗しました: {e}", "error")
            return redirect(url_for('worktime.worktime_view', team_id=team_id))
    else:
        flash("開始時間が不正な形式です。HH:MM 形式で入力してください。", "error")
        return redirect(url_for('worktime.worktime_view', team_id=team_id))

    if end_time_str and time_pattern.match(end_time_str):
        try:
            parts = end_time_str.split(':')
            end_time_obj = datetime.time(hour=int(parts[0]), minute=int(parts[1]), second=0)
        except ValueError as e:
            flash(f"終了時間の変換に失敗しました: {e}", "error")
            return redirect(url_for('worktime.worktime_view', team_id=team_id))
    else:
        flash("終了時間が不正な形式です。HH:MM 形式で入力してください。", "error")
        return redirect(url_for('worktime.worktime_view', team_id=team_id))

    current_team_id = team_id 
    Worktime.create(uid, current_team_id, start_time_obj, end_time_obj) 
    flash("勤怠が正常に記録されました。", "success")
    
    return redirect(url_for('worktime.worktime_view', team_id=team_id))

# 勤怠の表示
@worktime_bp.route('/<int:team_id>', methods=['GET'])
def worktime_view(team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))
    
    worktimes = Worktime.get_by_team_id(team_id)
    team_members = User.get_team_members(team_id)

    return render_template('work_time_log.html', worktimes = worktimes, team_id = team_id, team_members = team_members)
