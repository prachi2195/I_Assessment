# importing necessary libraries
import pandas as pd
# connecting mysql server
import pymysql
from sqlalchemy import create_engine

database = pymysql.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="hospital")
cursor = database.cursor()
query2 = "select * from patients"

# executing cursor
cursor.execute(query2)

# fetching tables
table_rows = cursor.fetchall()
df = pd.read_sql('SELECT * FROM patients', con=database)  # fitting into pandas dataframe
# print (df)
ans = df.loc[df['Country'] == "IND"]
countries = df['Country'].unique()

def show_data(country):
    data = df.loc[df['Country'] == country]
    print(data)


def create_country_table(country):
    data = df.loc[df['Country'] == country]
    file_name = str(country)
    cursor.execute('Create Table if not exists Table_{} like patients'.format(country))
    engine = create_engine('mysql+mysqldb://root:mysql@localhost:3306/hospital', echo=False)
    data.to_sql(name='table_'+country.lower(), con=engine, if_exists='append', index=False)
    database.commit()
    print("Table: Table_{} has been created.".format(country))

#calling the functions
for country in countries:
    show_data(country)
    create_country_table(country)