import psycopg

with psycopg.connect('dbname=test') as conn:
    with conn.cursor() as curs:
        # curs.execute("""
        #     create table things (id integer primary key,
        #         description varchar)
        #         """)
        curs.execute("insert into things (id) values (5)")
        curs.execute("insert into things (id, description) values (6, 'pears and lemons')")
        curs.execute("select * from things")
        print(curs.fetchall())
        conn.commit()