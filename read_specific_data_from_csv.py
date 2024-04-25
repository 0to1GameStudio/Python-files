import pandas as pd
from sqlalchemy import create_engine
import psycopg2 as pg2

file_name = r'D:\NikhilData\Desktop\Webpages\SQL TABLEAU\Task4.csv'
df = pd.read_csv(file_name)

#df = pd.read_csv(file_name)
def create_data_frame(df)->pd.DataFrame: # type: ignore
    column_names = ['gender','dept_name','avg_salary']
    result = pd.DataFrame(df,columns =column_names)
    print(result)

create_data_frame(df)

def retrieve_specific(df)->pd.DataFrame:
    column_names = ['gender','dept_name','avg_salary']
    ret_result = df[df['avg_salary'] <= 61963.6756]
    print('*'*50)
    print(ret_result)

retrieve_specific(df)

def retrieve_data(df)->pd.DataFrame:
    column_names = ['gender','dept_name','avg_salary']
    ret_s_data = df.loc[6,column_names]
    print('*'*20)
    print(ret_s_data)

retrieve_data(df)