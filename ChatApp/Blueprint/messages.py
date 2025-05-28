from flask import Blueprint, session, redirect, url_for, render_template, request
from ChatApp.models import Channel, Message

messages_bp = Blueprint('messages', __name__, url_prefix='/messages')

#@app.route ではなく、 @messages_bp.route を使用
#メッセージ表示
@messages_bp.route('/<int:team_id>/<int:cid>', methods=['GET'])
def detail(team_id, cid):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))

    channel = Channel.find_by_channel_id(cid)
    messages = Message.get_all(cid)

    return render_template('messages.html', messages=messages, channel=channel, uid=uid)

#メッセージ投稿
@messages_bp.route('/<int:team_id>/<int:cid>', methods=['POST'])
def create_message(team_id, cid):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))

    message = request.form.get('message')

    if message:
        Message.create(uid, cid, team_id, message)

    return redirect(url_for('messages.detail', team_id=team_id, cid=cid))

#メッセージ削除
@messages_bp.route('/<int:team_id>/<int:cid>/<message_id>', methods=['POST'])
def delete_message(team_id, cid, message_id):
    uid = session.get('user_id')
    if uid is None:
        return redirect(url_for('auth.login_page'))

    if message_id:
        Message.delete(message_id)
    return redirect('/channels/{cid}/messages'.format(cid = cid))