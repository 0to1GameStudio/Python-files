import psycopg2 as pg2
import pandas.io.sql as pd
from sqlalchemy import create_engine

alchemyEngine = create_engine('postgresql+psycopg2://postgres:nik123@127.0.0.1:5434/painting',pool_recycle=3600)
conn = alchemyEngine.connect()
try:
     files = ['artist', 'canvas_size', 'image_link', 'museum', 'museum_hours', 'product_size', 'subject', 'work']

     for file in files:
         df = pd.read_csv(f'D:/NikhilData/Desktop/Webpages/Python Practice/archive/{file}.csv')
         df.to_sql(file, con=conn, if_exists = 'replace', index = False)
         print("All Tables are created")
         ret = pd.read_sql_query('select * from artist',conn)
         print(ret)
    #data = pd.read_sql_query('select * from payment',con=alchemyEngine)
    #print(data.info())

except Exception as error:
    print(error)
