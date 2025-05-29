from flask import Blueprint, session, redirect, url_for, render_template, request, flash
from ChatApp.models import Channel, Team, Worktime, User

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

#@app.route ではなく、 @channels_bp.route を使用

# 統合ダッシュボード
@dashboard_bp.route('/<int:team_id>', methods=['GET'])
def dashboard_view(team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))

    # 共通のチーム名
    teamname = Team.get_teamname(team_id)['teamname']

    # チャンネル一覧
    channels = list(Channel.get_team_channels(team_id))
    channels.reverse()

    # 勤怠情報
    worktimes = Worktime.get_by_team_id(team_id)
    team_members = User.get_team_members(team_id)

    return render_template(
        'dashboard.html',
        team_id=team_id,
        teamname=teamname,
        channels=channels,
        worktimes=worktimes,
        team_members=team_members
    )
