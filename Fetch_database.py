import psycopg2 as pg2
import pandas as pd
from sqlalchemy import create_engine
#secret = 'nik123'
alchemyEngine = create_engine('postgresql+psycopg2://test:@127.0.0.1',pool_recycle=3600)
hostname = 'localhost'
database = 'dvdrental'
username = 'postgres'
pwd = 'nik123'
port_id = 5434
conn= None
cur = None
try:
    conn = pg2.connect(host = hostname,
                       dbname = database,
                       user = username,
                       password = pwd,
                       port = port_id)
    cur = conn.cursor()
    #data = pd.read_sql('select * from payment;',conn)
    #pd.set_option('display.expand_frame_repr',False)
    #data.head()
    cur.execute("select * from payment")
    print(cur.fetchone())

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    
    



