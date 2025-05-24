import os
import pymysql
import pymysql.cursors
from pymysqlpool.pool import Pool

class DB:
    @classmethod
    def init_db_pool(cls):
        pool = Pool(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database = os.getenv('DB_DATABASE'),
            max_size = 30,
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor,
        )

        pool.init()
        return pool