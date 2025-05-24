from flask import Blueprint, session, redirect, url_for, render_template, request, flash
from ChatApp.models import Channel

channels_bp = Blueprint('channels', __name__, url_prefix='/channels')

#@app.route ではなく、 @channels_bp.route を使用

# チーム内のチャンネルの表示
@channels_bp.route('/<int:team_id>', methods=['GET'])
def channels_view(team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))
    else:
        channels = Channel.get_team_channels(team_id)
        # channels.reverse()
        return render_template('channels.html', channels=channels, team_id=team_id)
    
# チャンネル作成
@channels_bp.route('/<int:team_id>/create', methods=['GET'])
def create_channel_page(team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))
    
    channel_name = request.form.get('channel_name')
    channel = Channel.find_by_channel_name(channel_name)
    if channel == None:
        channel_description = request.form.get('channel_description')
        Channel.create(channel_name, channel_description, team_id, uid)
        return redirect(url_for('channels.channels_view', team_id=team_id))
    else:
        error = "チャンネル名はすでに使用されています"
        return render_template('error/error.html', error_message=error)
    
# チャンネルの更新
@channels_bp.route('/<int:team_id>/update/<int:cid>', methods=['GET'])
def update_channel(cid,team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))
    
    channel_name = request.form.get('channel_name')
    channel_description = request.form.get('channel_description')

    Channel.update(channel_name, channel_description, cid)
    return redirect(url_for('channels.channels_view', team_id=team_id))

# チャンネルの削除
@channels_bp.route('/<int:team_id>/delete/<int:cid>', methods=['GET'])
def delete_channel(cid,team_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))
    
    channel = Channel.find_by_channel_id(cid)
    if channel["created_by"] != uid:
        flash('チャンネルは作成者のみ削除可能です')
    else:
        Channel.delete(cid)
    return redirect(url_for('channels.channels_view', team_id=team_id))

    
