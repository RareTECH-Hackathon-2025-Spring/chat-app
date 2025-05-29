# users のcreateを作る
from flask import abort
import pymysql
from ChatApp.util.DB import DB
from pymysql.cursors import DictCursor  # ← 追加

db_pool = DB.init_db_pool()

class User:
    @classmethod
    def create(cls, username, password, team_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "INSERT INTO users (username, password_hash, team_id) VALUES (%s, %s, %s);"
                    cur.execute(sql, (username, password, team_id))
                    conn.commit()
        except pymysql.MySQLError as e:
            print(f'Error creating user: {e}')
            abort(500)

    @classmethod
    def find_by_username(cls, username):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM users WHERE username=%s;"
                    cur.execute(sql, (username,))
                    user = cur.fetchone()
                return user
        except pymysql.MySQLError as e:
            print(f'Error creating user: {e}')
            abort(500)
    
    @classmethod
    def get_team_members(cls, team_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM users WHERE team_id=%s;"
                    cur.execute(sql,(team_id,))
                    team_members = cur.fetchall()
                return team_members
        except pymysql.MySQLError as e:
            print(f'Error creating user: {e}')
            abort(500)

class Team:
    @classmethod
    def get_all_teams(cls):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor(DictCursor) as cur:
                    sql = "SELECT id, teamname FROM teams ORDER BY teamname;"
                    cur.execute(sql)
                    teams = cur.fetchall()
                return teams
        except pymysql.MySQLError as e:
            print(f'Error creating user: {e}')
            abort(500)
            
    @classmethod
    def get_teamname(cls, team_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor(DictCursor) as cur:
                    sql = "SELECT teamname FROM teams WHERE id=%s;"
                    cur.execute(sql,(team_id,))
                    teamname = cur.fetchone()
                    return teamname
        except pymysql.MySQLError as e:
            print(f'Error creating user: {e}')
            abort(500)

class Channel:

    # チャンネルの作成
    @classmethod
    def create(cls, name, description, team_id, user_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "INSERT INTO channels (channel_name, channel_description, team_id, created_by) VALUES (%s, %s, %s, %s);"
                    cur.execute(sql, (name, description, team_id, user_id))
                    conn.commit()
        except pymysql.MySQLError as e:
            print(f'Error creating channel: {e}')
            abort(500)

    # チャンネルの取得
    @classmethod
    def get_team_channels(cls, team_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "SELECT id, channel_name, channel_description FROM channels WHERE team_id = %s;"
                    cur.execute(sql, (team_id,))
                    channels = cur.fetchall()
                    return channels
        except pymysql.MySQLError as e:
            print(f'Error fetching channels: {e}')
            abort(500)

    # チャンネルの更新
    @classmethod
    def update(cls, name, description, channel_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "UPDATE channels SET channel_name = %s, channel_descritption = %s WHERE id = %s;"
                    cur.execute(sql, (name, description, channel_id,))
                    conn.commit()
        except pymysql.MySQLError as e:
            print(f'Error updating channel: {e}')
            abort(500)
    
    # チャンネルの削除
    @classmethod
    def delete(cls, channel_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "DELETE FROM channels WHERE id = %s;"
                    cur.execute(sql, (channel_id,))
                    conn.commit()
        except pymysql.MySQLError as e:
            print(f'Error deleting channel: {e}')
            abort(500)

    # チャンネルIDでの取得
    @classmethod
    def find_by_channel_id(cls, channel_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM channels WHERE id = %s;"
                    cur.execute(sql, (channel_id,))
                    channel = cur.fetchone()
                    return channel
        except pymysql.MySQLError as e:
            print(f'Error fetching channel by ID: {e}')
            abort(500)

    # チャンネル名での取得
    @classmethod
    def find_by_channel_name(cls, channel_name):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM channels WHERE channel_name = %s;"
                    cur.execute(sql, (channel_name,))
                    channel = cur.fetchone()
                    return channel
        except pymysql.MySQLError as e:
            print(f'Error fetching channel by ID: {e}')
            abort(500)

class Worktime:

    # 作成
    @classmethod
    def create(cls, team_id, user_id, work_date, start_time, end_time):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "INSERT INTO worktimes (user_id, team_id, work_date, start_time, end_time) VALUES (%s, %s, %s, %s, %s);"
                    cur.execute(sql, (user_id, team_id, work_date, start_time, end_time,))
                    conn.commit()
        except pymysql.MySQLError as e:
            print(f'Error creating worktime: {e}')
            abort(500)

    # 個人単位の取得
    @classmethod
    def get_by_user_id(cls, user_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM worktimes WHERE user_id = %s;"
                    cur.execute(sql, (user_id,))
                    worktime = cur.fetchone()
                    return worktime
        except pymysql.MySQLError as e:
            print(f'Error creating worktime: {e}')
            abort(500)

    # チーム単位の取得
    @classmethod
    def get_by_team_id(cls, team_id):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = """
                    SELECT
                        users.username,
                        worktimes.work_date,
                        worktimes.start_time,
                        worktimes.end_time
                    FROM worktimes 
                    INNER JOIN users ON worktimes.user_id = users.id
                    WHERE worktimes.team_id = %s;"""
                    cur.execute(sql, (team_id,))
                    worktimes = cur.fetchall()
                    return list(worktimes) if worktimes else []
        except pymysql.MySQLError as e:
            print(f'Error creating worktime: {e}')
            abort(500)


    # 更新
    @classmethod
    def update(cls, user_id, work_date, start_time, end_time):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "UPDATE worktimes SET work_date=%s, start_time = %s, end_time = %s WHERE user_id = %s;"
                    cur.execute(sql, (work_date, start_time, end_time, user_id,))
                    conn.commit()
        except pymysql.MySQLError as e:
            print(f'Error creating worktime: {e}')
            abort(500)

# Message Class
class Message:
    # メッセージ一覧取得
    @classmethod
    def get_all(cls, cid):
        try:
            with db_pool.get_conn() as conn:
                with conn.cursor(pymysql.cursors.DictCursor) as cur:
                    sql = """
                    SELECT
                        messages.id,
                        messages.user_id AS uid,
                        messages.channel_id,
                        messages.content AS message,
                        users.username AS user_name
                    FROM messages
                    INNER JOIN users ON messages.user_id = users.id
                    WHERE messages.channel_id = %s
                    ORDER BY messages.created_at ASC;
                    """
                    cur.execute(sql, (cid,))
                    channels = cur.fetchall()
                    return channels
        except pymysql.Error as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
    
    #メッセージ投稿
    @classmethod
    def create(cls, uid, cid, team_id, message):
       try:
            print("1. Connecting to DB")
            with db_pool.get_conn() as conn:
                print("2. Got connection")
                with conn.cursor() as cur:
                    print("3. Got cursor")
                    sql = "INSERT INTO messages (user_id, channel_id, team_id, content) VALUES(%s, %s, %s, %s)"
                    print(f"4. Executing SQL: {sql}")
                    cur.execute(sql, (uid, cid, team_id, message,))
                    print("5. Executed SQL")
                    conn.commit()
                    print("6. Committed")
       except pymysql.Error as e:
            print("7. Caught MySQL Error")
            print(f'エラーが発生しています：{e}')
            abort(500)

    @classmethod
    def delete(cls, message_id):
       try:
           with db_pool.get_conn() as conn:
                with conn.cursor() as cur:
                    sql = "DELETE FROM messages WHERE id=%s;"
                    cur.execute(sql, (message_id,))
                    conn.commit()
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)