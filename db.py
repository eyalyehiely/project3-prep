import psycopg2
def query(sql):
    with psycopg2.connect(
        database="postgres",
        host="localhost",
        user="postgres",
        password="postgres",
        port="5432") as conn:
        cur=conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
      
