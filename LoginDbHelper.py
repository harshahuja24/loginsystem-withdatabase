from pymysql import *


def get_data(query, parameters=None):
    conn = connect(host='localhost', database='project', user='root', password='ahuja24')
    cur = conn.cursor()

    if parameters is None:
        cur.execute(query)

    else:
        cur.execute(query, parameters)

    result = cur.fetchone()
    print(result)
    cur.close()
    conn.close()
    return result

def execute_query(query, parameters=None):
    conn = connect(host='localhost',database='project',user='root',password='ahuja24')
    cur = conn.cursor()
    if ( parameters is None):
        cur.execute(query, parameters)
    else:
        cur.execute(query,parameters)
    conn.commit()
    cur.close()
    conn.close()