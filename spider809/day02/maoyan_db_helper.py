import pymysql


# 取数据库连接
def get_connection():
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = '123456'
    database = 'maoyan9'
    db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
    return db


# 取数据库游标
def get_cursor(db):
    cursor = db.cursor()
    return cursor


# 关闭数据库连接
def close_connection(db):
    db.close()


# 执行sql语句
def execute_sql(db, cursor, item_dict):
    sql = 'insert into movie (movie_name, actor, releasetime, cover_url, score, rank, detail_url) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (item_dict['movie_name'], item_dict['actor'], item_dict['releasetime'], item_dict['cover_url'], item_dict['score'], item_dict['rank'], item_dict['detail_url'])

    cursor.execute(sql)
    db.commit()


def execute_sql2(db, cursor, item_dict):
    sql = 'insert into movie (movie_name, actor, releasetime, cover_url, score, rank, detail_url) values (%s, %s, %s, %s, %s, %s, %s)'

    cursor.execute(sql, (item_dict['movie_name'], item_dict['actor'], item_dict['releasetime'], item_dict['cover_url'], item_dict['score'], item_dict['rank'], item_dict['detail_url']))
    db.commit()
