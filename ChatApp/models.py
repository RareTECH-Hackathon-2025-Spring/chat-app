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