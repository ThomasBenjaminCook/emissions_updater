import pandas as pd
from sqlalchemy import create_engine
from updater import update
from recent_date import get_recent_date
import datetime as dt

total_reset = False #If this is set to true, the whole database will be reset from scratch. This might be used if the emissions data changes.

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="ThomasAppMaker",
    password="P_R5nvjG5DV4Vd6",
    hostname="ThomasAppMaker.mysql.pythonanywhere-services.com",
    databasename="ThomasAppMaker$ipcollect",
)
engine = create_engine(SQLALCHEMY_DATABASE_URL) #Creates the object which must be passed to Pandas to interact with database.

df = pd.read_sql_table("emissions_database", con=engine, index_col="index") #The dataframe created based on the database uses the column 'index' as the index column. This means the column dissapears. 

if(total_reset):
    most_recent_date = dt.datetime.strptime("2000-01-01 00:00:00","%Y-%m-%d %H:%M:%S") #If total reset is selected, new data will be collected, and the computer will search as far back as the year 2000.
else:
    most_recent_date = get_recent_date(df)

df = update(df,most_recent_date) #Updates the database, given that the date to crawl from is most_recent_date.

df.to_sql("emissions_database", con=engine, if_exists="replace") 